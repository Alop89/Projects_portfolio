from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import logging

logging.basicConfig(
    level = logging.INFO, 
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S", 
    filename = "api.log", 
    filemode = "w"
)

# Incio de app 
app = FastAPI(
    title = "Trial early warning system", 
    version = "1.0", 
)

try:
    import os
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    MODEL_PATH = os.path.join(base_dir, 'src', 'models', 'clinical_xgboost_pipeline.pkl')
    pipeline = joblib.load(MODEL_PATH)
    logging.info(f"Modelo cargado en memoria desde el path: {MODEL_PATH}")


except FileNotFoundError:
    logging.error(f"Archivo no encontrado en el path")
    raise RuntimeError("Error al cargar el pipeline")

# Datos 
class PatientData(BaseModel):
    "Validación automatica de datos"
    age: int = Field(..., ge=0, le=100, description = "Edad del paciente")
    gender: str = Field(...,description = "Male o Female")
    treatment_arm: str = Field(..., description = "Experimental, Standard_Care o Placebo")
    baseline_bmi: float = Field(..., gt = 10.0, description = "IMC del paciente al iniciar el estudio")
    alt_enzyme_level: float = Field(..., gt=0.0, description = "Nivel de enzima hepática ALT")
    wbc_count: float = Field(..., gt =0.0, description = "Conteo de glóbulos blancos")
    comorbidity_index: int = Field(..., ge =0, le = 5, description = "Número de comorbilidades")


@app.get("/")
def root():
    return {"message": "Bienvenido a: Early Warning System API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict/xgboost")
def predict_sae_risk(patient: PatientData):
    """Carga los datos del paciente y devuelve la predicción de toxicidad."""
    try:
        # Conversion a DataFrame
        patient_dict = patient.model_dump()
        df_input = pd.DataFrame([patient_dict])

        # Inferencia
        probability = pipeline.predict_proba(df_input)[0,1]

        # umbral critico
        threshold = 0.0878
        risk = bool(probability >= threshold)

        return {
            "status":"success",
            "model_revision": "XGBoost-1.0",
            "risk_probability": round(float(probability),4),
            "is_at_high_risk": risk, 
            "recommended_action":"Monitoreo intensivo" if risk else "Protocolo estándar"
        }


    except Exception as e:
        logging.error(f"Error en la predicción: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))