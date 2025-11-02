from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_iris


# MODEL_PATH = "application/artifacts/svm_iris_model.joblib" 
MODEL_PATH = "artifacts/svm_iris_model.joblib" 


# --- 2. FastAPI Setup ---

app = FastAPI(title="IRIS CD API", version="1.0")

# Input schema for Pydantic validation
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Load the trained model on startup
try:
    classifier = joblib.load(MODEL_PATH)
    IRIS_TARGET_NAMES = load_iris().target_names.tolist()
except FileNotFoundError:
    raise RuntimeError(f"Model file not found at {MODEL_PATH}. Run the app script once to generate it.")


@app.get("/", tags=["Health"])
def health_check():
    """Simple health check endpoint."""
    return {"status": "OK", "model_loaded": True, "version": app.version}


@app.post("/predict", tags=["Prediction"])
def predict(data: IrisInput):
    """
    Predicts the Iris species based on four features.
    """
    # Convert Pydantic model to numpy array
    input_data = np.array([
        [data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]
    ])
    
    predicted_species = classifier.predict(input_data)[0]
    print(predicted_species)
    return {
        "prediction": predicted_species,
        "version": 1,
        "input_features": data.model_dump()
    }
