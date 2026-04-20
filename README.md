# Heart Disease MLOps

Predicción de falla cardíaca con un flujo MLOps local: entrenamiento con scikit-learn, API con FastAPI, contenerización con Docker, orquestación con Kubernetes, CI con GitHub Actions y monitoreo de deriva con Evidently.

## Tecnologías

- **scikit-learn**: pipeline de entrenamiento con `Pipeline` y `GridSearchCV`
- **FastAPI**: API REST para predicciones en tiempo real
- **Docker**: contenerización de la aplicación
- **Kubernetes (Minikube)**: orquestación local
- **GitHub Actions**: integración continua (lint + tests)
- **Evidently**: monitoreo de deriva de datos

## Estructura

```
heart-disease-mlops/
├── app/
│   └── api.py
├── docker/
│   ├── Dockerfile
│   └── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── notebooks/
│   ├── 1_model_leakage_demo.ipynb
│   └── 2_model_pipeline.ipynb
├── tests/
│   └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── drift_report.py
├── drift_report.html
├── model.joblib
└── README.md
```

## Uso

### Instalación

```bash
pip install -r docker/requirements.txt
```

### Entrenamiento

Ejecutar los notebooks en orden:

1. `notebooks/1_model_leakage_demo.ipynb`
2. `notebooks/2_model_pipeline.ipynb`

El pipeline final se guarda en `app/model.joblib`.

### API local

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000
```

### Docker

```bash
docker build -t heart-api -f docker/Dockerfile .
docker run -p 8000:8000 heart-api
```

### Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get svc
```

### Predicción

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Age": 54, "Sex": "M", "ChestPainType": "ATA",
    "RestingBP": 140, "Cholesterol": 220, "FastingBS": "0",
    "RestingECG": "Normal", "MaxHR": 150, "ExerciseAngina": "N",
    "Oldpeak": 1.2, "ST_Slope": "Up"
  }'
```

### Pruebas

```bash
pytest tests/
```

### Monitoreo de deriva

```bash
python drift_report.py
```

Genera `drift_report.html` con la comparación entre los datos de entrenamiento (referencia) y los de prueba (actual).

## CI/CD

El workflow `.github/workflows/ci.yml` se ejecuta en cada `push` y realiza lint con `flake8` y pruebas con `pytest`.
