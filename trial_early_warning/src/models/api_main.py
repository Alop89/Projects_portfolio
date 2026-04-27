from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Clinical Oracle API", version="1.0.0")


class PatientData(BaseModel):
    age: int
    gender: str
    treatment_arm: str
    baseline_bmi: float
    alt_enzyme_level: float
    wbc_count: float
    comorbidity_index: int


try:
    xgb_pipeline = joblib.load("clinical_xgboost_pipeline.pkl")

except Exception as e:
    raise RuntimeError(f"Error cargando modelos: {e}")

@app.get("/health")
def health_check():
    """Endpoint vital para balanceadores de carga en la nube."""
    return {"status": "healthy", "service": "Clinical Oracle API"}

@app.post("/predict/xgboost")
def predict_risk(patient: PatientData):
    """Recibe datos del paciente y retorna la probabilidad de SAE."""
    try:
 
        df = pd.DataFrame([patient.model_dump()])
        prob = xgb_pipeline.predict_proba(df)[0, 1]
        
        return {
            "model_used": "XGBoost",
            "risk_probability": float(prob),
            "threshold_flag": bool(prob >= 0.0878)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))