from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

model = joblib.load("app/model.joblib")
app = FastAPI()

class Input(BaseModel):
    Age: int
    Sex: str
    ChestPainType: str
    RestingBP: int
    Cholesterol: int
    FastingBS: str    
    RestingECG: str
    MaxHR: int
    ExerciseAngina: str
    Oldpeak: float
    ST_Slope: str

@app.post("/predict")
def predict(data: Input):
    try:
        X = pd.DataFrame([data.model_dump()])
        proba = model.predict_proba(X)[0][1]
        return {
            "heart_disease_probability": round(float(proba), 4),
            "prediction": int(proba > 0.5)
        }
    except Exception as e:
        return {"error": str(e)}