# **Heart Disease MLOps**

Predicción de enfermedad cardíaca mediante un flujo MLOps local, integrando entrenamiento con scikit-learn, despliegue con FastAPI, contenerización con Docker, orquestación con Kubernetes, CI con GitHub Actions y monitoreo de deriva con Evidently.

## Descripción general

Este proyecto implementa un flujo completo de Machine Learning Operations (MLOps) para la predicción de enfermedad cardíaca a partir de variables clínicas y demográficas. Se desarrollan notebooks para el análisis del problema, la detección de data leakage, la construcción de pipelines de preprocesamiento y modelado, así como la comparación de distintos algoritmos de clasificación.

Además, el proyecto incorpora una API para servir predicciones, archivos de despliegue local, pruebas automáticas e integración continua. Como complemento, se construyó un Jupyter Book para documentar y presentar el desarrollo del proyecto de manera estructurada.

## Video de demostración

Se incluye un video donde se muestra el sistema en funcionamiento y el flujo MLOps en producción:

**Video:** https://drive.google.com/file/d/196u_4XiWJGrtcg4vgdAxwkHL5IoPxUfU/view?usp=drivesdk

## Tecnologías utilizadas

- **scikit-learn**: entrenamiento de modelos, pipelines y búsqueda de hiperparámetros con `Pipeline` y `GridSearchCV`
- **FastAPI**: construcción de la API REST para predicciones en tiempo real
- **Docker**: contenerización del servicio
- **Kubernetes (Minikube)**: despliegue local del contenedor
- **GitHub Actions**: integración continua con linting y pruebas
- **Evidently**: monitoreo de deriva de datos
- **Jupyter Book**: documentación interactiva del proyecto

## Estructura del proyecto

```text
heart-disease-mlops/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .vscode/
├── app/
│   ├── __init__.py
│   ├── api.py
│   └── model.joblib
├── book/
│   ├── _build/
│   ├── notebooks/
│   │   ├── 1_model_leakage_demo.ipynb
│   │   ├── 2_model_pipeline.ipynb
│   │   └── model.joblib
│   ├── _config.yml
│   ├── _toc.yml
│   ├── intro.md
│   ├── video.md
│   └── Uninorte_Logo.png
├── docker/
│   ├── Dockerfile
│   └── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── notebooks/
│   ├── data/
│   ├── 1_model_leakage_demo.ipynb
│   └── 2_model_pipeline.ipynb
├── tests/
│   └── test_api.py
├── drift_report.py
├── drift_report.html
└── README.md
```

## Flujo del proyecto 

El proyecto se desarrolla en varias etapas:

1. Exploración del dataset y detección de data leakage
2. Preprocesamiento y modelado seguro con pipelines
3. Comparación de modelos de clasificación
4. Exportación del mejor modelo
5. Construcción de API con FastAPI
6. Contenerización con Docker
7. Despliegue con Kubernetes
8. Automatización con GitHub Actions
9. Monitoreo con Evidently
10. Documentación con Jupyter Book

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

## Autoras:
- Mariangel Yepes
- Alejandra Meneses
- Daniela Hernández
- Valeria Incer
