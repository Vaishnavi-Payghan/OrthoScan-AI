from flask import Flask, request, jsonify
from tensorflow.keras.applications.resnet50 import preprocess_input
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

# =========================
# Load trained model
# =========================

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "resnet50_finetuned.keras"
)

model = tf.keras.models.load_model(MODEL_PATH)

print("✅ Fine-tuned model loaded successfully!")


# =========================
# Preprocessing
# =========================

from tensorflow.keras.applications.resnet50 import preprocess_input


def preprocess_image(image):

    image = image.convert("RGB")

    original_width, original_height = image.size

    target_size = 224

    scale = min(
        target_size / original_width,
        target_size / original_height
    )

    new_width = int(original_width * scale)
    new_height = int(original_height * scale)

    image = image.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS
    )

    canvas = Image.new(
        "RGB",
        (target_size, target_size),
        (0, 0, 0)
    )

    left = (target_size - new_width) // 2
    top = (target_size - new_height) // 2

    canvas.paste(image, (left, top))

    # Convert to numpy
    image_array = np.array(canvas).astype("float32")

    # IMPORTANT:
    # Same preprocessing used during ResNet50 training
    image_array = preprocess_input(image_array)

    # Batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    return image_array
# =========================
# Prediction API
# =========================

@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "error": "No file selected"
        }), 400

    try:

        image = Image.open(file)

        image_array = preprocess_image(image)

        # Model prediction
        output = float(
            model.predict(
                image_array,
                verbose=0
            )[0][0]
        )

        # Your selected threshold
        threshold = 0.50

        if output < threshold:

            result = "FRACTURED"
            confidence = (1 - output) * 100

        else:

            result = "NON-FRACTURED"
            confidence = output * 100
        print("🔥 MODEL OUTPUT:", output)
        print("🔥 RESULT:", result)
        print("🔥 CONFIDENCE:", confidence)

        return jsonify({

            "result": result,

            "confidence": round(
                confidence,
                2
            ),

            "model_output": round(
                output,
                6
            )

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# =========================
# Run Flask
# =========================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )