from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health_check():
    """Valida que la API esté viva."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "Clinical Oracle API"}

def test_predict_endpoint():
    """Simula una petición POST y valida la respuesta del modelo."""
    payload = {
        "age": 65,
        "gender": "Male",
        "treatment_arm": "Experimental",
        "baseline_bmi": 28.5,
        "alt_enzyme_level": 45.2,
        "wbc_count": 8.1,
        "comorbidity_index": 2
    }
    response = client.post("/predict/xgboost", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "risk_probability" in data
    assert isinstance(data["risk_probability"], float)