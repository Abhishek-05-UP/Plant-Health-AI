
import json
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

# -------------------------------
# 1. Page configuration
# -------------------------------
st.set_page_config(
    page_title="Plant Health AI",
    page_icon="🌱",
    layout="centered"
)

# -------------------------------
# 2. Load the trained AI model
# -------------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("plant_model (1).keras")

    with open("class_names.json", "r", encoding="utf-8") as file:
        class_names = json.load(file)

    return model, class_names


st.title("🌱 Plant Health AI")
st.write(
    "Upload a plant leaf image to identify the model's "
    "predicted plant disease."
)

# Load model safely
try:
    model, class_names = load_model()
except Exception as error:
    st.error(f"Unable to load the AI model: {error}")
    st.stop()

# -------------------------------
# 3. Upload a leaf image
# -------------------------------
uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(
            image,
            caption="Uploaded plant leaf",
            use_container_width=True
        )

    except Exception:
        st.error("Unable to read this image. Please upload another image.")
        st.stop()

    # -------------------------------
    # 4. Analyze the image
    # -------------------------------
    if st.button("🔍 Analyze Plant", type="primary"):

        with st.spinner("Analyzing your plant image..."):

            # Resize image to the model's required dimensions
            resized_image = image.resize((224, 224))

            # Convert image to a NumPy array
            image_array = np.array(
                resized_image,
                dtype=np.float32
            )

            # Add batch dimension
            image_array = np.expand_dims(image_array, axis=0)

            # Apply MobileNetV2 preprocessing
            image_array = (
                tf.keras.applications.mobilenet_v2.preprocess_input(
                    image_array
                )
            )

            # Get predictions
            predictions = model.predict(
                image_array,
                verbose=0
            )[0]

            # Find the three highest-scoring classes
            top_indices = np.argsort(predictions)[-3:][::-1]

            predicted_index = int(top_indices[0])
            predicted_class = class_names[predicted_index]
            confidence = float(predictions[predicted_index]) * 100

        # -------------------------------
        # 5. Display the main prediction
        # -------------------------------
        st.subheader("🌿 AI Prediction")

        readable_class = predicted_class.replace(
            "___", " — "
        ).replace("_", " ")

        st.success(readable_class)

        st.metric(
            "Top prediction score",
            f"{confidence:.2f}%"
        )

        # Warn about uncertain predictions
        if confidence < 70:
            st.warning(
                "The model may be uncertain about this image. "
                "The prediction could be incorrect. Try a clearer "
                "leaf photo with good lighting and a plain background."
            )

        # -------------------------------
        # 6. Display the top 3 predictions
        # -------------------------------
        st.subheader("📊 Top 3 Predictions")

        for index in top_indices:

            label = class_names[int(index)]
            readable_label = label.replace(
                "___", " — "
            ).replace("_", " ")

            score = float(predictions[index])

            st.write(
                f"**{readable_label}** — {score * 100:.2f}%"
            )

            st.progress(score)

        # -------------------------------
        # 7. Important disclaimer
        # -------------------------------
        st.caption(
            "Note: These are AI predictions, not confirmed diagnoses. "
            "The model was trained on PlantVillage images, so accuracy "
            "may be lower on real-world photographs. A high score does "
            "not guarantee a correct result."
        )
