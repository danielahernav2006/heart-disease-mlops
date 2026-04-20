"""Prueba básica funcional de la API."""

from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_predict_endpoint():
    payload = {
        "Age": 54,
        "Sex": "M",
        "ChestPainType": "ATA",
        "RestingBP": 140,
        "Cholesterol": 220,
        "FastingBS": "0",
        "RestingECG": "Normal",
        "MaxHR": 150,
        "ExerciseAngina": "N",
        "Oldpeak": 1.2,
        "ST_Slope": "Up",
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "heart_disease_probability" in body
    assert "prediction" in body
