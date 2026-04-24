import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# Variables globales 
UMBRAL_CLINICO = 0.204 # Optimizado para F2-Score (Alto Recall)
MODEL_PATH = '../models/clinical_oracle_pipeline.pkl'
DATA_PATH = '../../data/raw/clinical_trial_data.csv'

# Configuración de la página
st.set_page_config(
    page_title="Clinical oracle| Riesgo de abandono de ensayos clínicos",
    page_icon="🥼",
    layout="wide",
)



# Carga de recursos en cache 
@st.cache_resource
def load_system_assets():
    try:
        #Preparación de datos
        pipeline = joblib.load(MODEL_PATH)
        df_background = pd.read_csv(DATA_PATH)
        X_bg_raw= df_background.drop(['Dropped_Out', 'Patient_ID'], axis=1)
        preprocessor = pipeline.named_steps['preprocessor']
        classifier = pipeline.named_steps['classifier']
        X_bg_transformed = preprocessor.transform(X_bg_raw)
        
        # Reconstrucción de nombres
        numeric_features = ['Age', 'BMI', 'Systolic_BP', 'Glucose_Level']
        cat_features = preprocessor.named_transformers_['cat'].get_feature_names_out(['Gender', 'Treatment_Arm'])
        feature_names = numeric_features + list(cat_features)

        # SHap explainer
        explainer = shap.Explainer(classifier, X_bg_transformed, feature_names=feature_names)

        return pipeline, explainer, feature_names
        
    except Exception as e:
        st.error(f"Error al cargar activos del sistema: {str(e)}")
        return None, None, None
    
# Ejecución de carga 
pipeline, explainer, feature_names = load_system_assets()

# Manejo de errores críticos
if pipeline is None:
    st.error("Error crítico: No se pudo cargar el modelo o los datos de referencia. Revise la configuración.")
    st.stop()


# Interfaz de usuario 
st.title("Clinical Oracle")
st.markdown("""
**Sistema predictivo de soporte clínico.** Ingrese los biomarcadores del paciente para evaluar su riesgo de abandonar el ensayo clínico.
El sistema utiliza un umbral de alta sensibilidad (20.4%) para erradicar falsos negativos.
""")

st.sidebar.header("📋 Ficha del paciente")

age = st.sidebar.slider("Edad (Años)", 18, 90, 55)
bmi = st.sidebar.slider("BMI", 15.0, 45.0, 28.0, 0.1)
sys_bp = st.sidebar.slider("Presión sistólica", 90, 180, 120)
glucose = st.sidebar.slider("Glucosa", 60, 200, 100)
gender = st.sidebar.selectbox("Género", ["M", "F"])
treatment = st.sidebar.selectbox("Tratamiento", ["Placebo", "Drug_X"])


input_data = pd.DataFrame({
    "Age": [age],   
    "BMI": [bmi],   
    "Systolic_BP": [sys_bp],   
    "Glucose_Level": [glucose],   
    "Gender": [gender],   
    "Treatment_Arm": [treatment]
})

# Motor de inferencia 
st.write("---PANTALLA DE RESULTADOS---")

if st.sidebar.button("Evaluar paciente", type="primary"):
    with st.spinner("Procesando historial clínico..."):
        probability = pipeline.predict_proba(input_data)[0][1]
        risk_label = probability >= UMBRAL_CLINICO
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Estado de riesgo")
            st.metric(label = "Probabilidad calculada", value = f"{probability:.2%}")

            if risk_label:
                st.error(" ⚠️Paciente con alto riesgo de abandono")
                
            else:
                st.success("✅ Paciente con bajo riesgo de abandono")
        with col2:
            st.subheader("Razonamiento del modelo (SHAP)")
            # Transformación y extracción de valores 
            X_transformed = pipeline.named_steps['preprocessor'].transform(input_data)
            shap_values = explainer(X_transformed)
            # Renderizado 
            fig, ax = plt.subplots(figsize=(6, 4))
            shap.plots.waterfall(shap_values[0], show=False)
            st.pyplot(fig)
            
            # Prevenir fugas de memoria limpiando la figura
            plt.close(fig)

    
    