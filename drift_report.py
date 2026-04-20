"""Etapa 6: Monitoreo de deriva de datos con Evidently."""

import pandas as pd
from sklearn.model_selection import train_test_split

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset


df = pd.read_csv("notebooks/data/heart.csv")
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

X_train, X_test, _, _ = train_test_split(X, y, test_size=0.2, random_state=42)

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=X_train, current_data=X_test)
report.save_html("drift_report.html")

print("Reporte generado: drift_report.html")
