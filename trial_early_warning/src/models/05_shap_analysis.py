import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt
import logging
import joblib

logging.basicConfig(
    level = logging.INFO, 
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%Y-%m-%d %H:%M:%S", 
    filename="clinical_shap_analysis.log", 
    filemode="w"
)


def run_shap_analysis(X_test, pipeline_final):
    """
    Audita el modelo XGBoost utilizando SHAP para explicabilidad Global y Local.
    """
    logging.info("Iniciando el análisis SHAP...")

    try:
        # Componenetes del pipline
        preprocessor = pipeline_final.named_steps['preprocessor']
        xgb_model = pipeline_final.named_steps['classifier']

        # Transformación de datos 
        X_test_processed = preprocessor.transform(X_test)
        
        # Nombres de columnas
        num_features = X_test.select_dtypes(include='number').columns.tolist()
        cat_features = X_test.select_dtypes(include = ['object','string']).columns.tolist()

        cat_encoder = preprocessor.named_transformers_['cat'].named_steps['encoder']
        cat_names = cat_encoder.get_feature_names_out(cat_features)
        features_names = num_features + list(cat_names)

        # Explicador SHAP 
        explainer = shap.TreeExplainer(xgb_model)
        
        # Usar la nueva API para obtener el objeto Explanation necesario para plots
        shap_explanation = explainer(X_test_processed)
        shap_explanation.feature_names = features_names

        # Grafico de beeswarm 
        plt.figure(figsize=(10,6))
        shap.plots.beeswarm(shap_explanation, max_display = 10, show = False)
        plt.title("Análisis global: ¿Qué biomarcadores impulsan el riesgo de SAE?", pad=20, fontweight='bold')
        plt.tight_layout()
        plt.show()
        

        # Grafico local waterfall 
        y_probs = xgb_model.predict_proba(X_test_processed)[:, 1]
        paciente_critico_idx = np.argmax(y_probs)
        
        plt.figure(figsize=(10, 6))
        shap.plots.waterfall(shap_explanation[paciente_critico_idx], show=False)
        plt.title(f"Análisis Local (Caja de Cristal): Paciente Crítico #{paciente_critico_idx}", pad=20, fontweight='bold')
        plt.tight_layout()
        plt.show()
        logging.info("Análisis SHAP completado exitosamente")

    except Exception as e: 
        logging.error(f"Error en el análisis SHAP: {e}")
        raise


if __name__ == "__main__":
    logging.info("Preparando datos y modelo para análisis SHAP...")
    
    try:
        data_eng = __import__('03_data_engineering')
        _, X_test, _, _, _ = data_eng.run_engineering_pipeline()
        model_path = 'clinical_xgboost_pipeline.pkl'
        pipeline_final = joblib.load(model_path)
        logging.info(f"Pipeline cargado exitosamente desde: {model_path}")
    
        run_shap_analysis(X_test, pipeline_final)
        
    except FileNotFoundError as e:
        logging.error(f"Archivo no encontrado: {e}. Asegúrate de ejecutar las fases previas.")
    except Exception as e:
        logging.error(f"Ocurrió un error al preparar el entorno SHAP: {e}")
