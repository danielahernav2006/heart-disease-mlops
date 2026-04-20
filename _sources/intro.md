# Predicción de enfermedad cardíaca mediante pipelines y MLOps

Este proyecto desarrolla un flujo completo de MLOps para la predicción de enfermedad cardíaca utilizando técnicas de aprendizaje supervisado, pipelines de preprocesamiento y herramientas modernas de despliegue y monitoreo.

El objetivo principal es construir un modelo capaz de identificar pacientes con riesgo de enfermedad cardíaca a partir de variables clínicas y demográficas, integrando buenas prácticas de Machine Learning desde la exploración inicial de los datos hasta la exportación y despliegue del modelo final.

El conjunto de datos utilizado contiene variables relacionadas con edad, sexo, presión arterial, colesterol, frecuencia cardíaca máxima, dolor en el pecho, resultados electrocardiográficos y otros factores clínicos relevantes. A partir de estas variables se plantea un problema de clasificación binaria en el que se busca predecir la presencia o ausencia de enfermedad cardíaca.

A lo largo del proyecto se implementan diferentes algoritmos de clasificación, incluyendo regresión logística, máquinas de soporte vectorial, Random Forest, Gradient Boosting y KNN. Además, se emplean técnicas de validación cruzada y búsqueda de hiperparámetros mediante GridSearchCV para identificar el mejor modelo.

El proyecto también incorpora componentes fundamentales de MLOps, como el desarrollo de una API con FastAPI, la contenedorización con Docker, el despliegue mediante Kubernetes, la automatización con GitHub Actions y el monitoreo de drift con Evidently.

## Contenido

- Demostración de data leakage y comparación de escenarios incorrectos y correctos
- Construcción de pipelines de preprocesamiento y modelado
- Entrenamiento y comparación de múltiples algoritmos de clasificación
- Optimización de hiperparámetros mediante GridSearchCV
- Exportación del mejor modelo entrenado
- Construcción de una API con FastAPI
- Contenerización con Docker
- Despliegue con Kubernetes
- Integración continua con GitHub Actions
- Monitoreo de drift y desempeño con Evidently