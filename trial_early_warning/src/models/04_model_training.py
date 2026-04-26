import pandas as pd
import numpy as np
import logging
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import (
    classification_report, 
    confusion_matrix, 
    roc_auc_score, 
    precision_recall_curve
)
from xgboost import XGBClassifier


logging.basicConfig(
    level = logging.INFO, 
    filename = "clinical_model_training.log",
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode ='a'
)

def train_and_evaluate_model(X_train, X_test, y_train, y_test, preprocessor):
    """
    Entrena el modelo XGBoost con GridSearchCV, y optimiza los hiperparámetros y ajusta 
    el umbral de decisión. 
    """
    try:

        #Integración de pipeline
        pipeline = Pipeline(
            steps = [
                ('preprocessor', preprocessor),
                ('classifier', XGBClassifier(random_state =21, eval_metric ='logloss'))
            ]
        )

        # Validación cruzada 
        param_grid = {
            'classifier__n_estimators' :[50,100],
            'classifier__max_depth': [3,5],
            'classifier__learning_rate' :[0.05,0.01],
            'classifier__scale_pos_weight' :[1,5]
        }
        
        # Validación cruzada estratificada 
        cv = StratifiedKFold(n_splits= 5, shuffle = True, random_state=21)
        logging.info("Iniciando GridSearchCV...")

        # Gridsearch 
        grid_search = GridSearchCV(
            pipeline, 
            param_grid=param_grid,
            cv = cv, 
            scoring = "roc_auc",  # Priorizar la correcta separación de clases. 
            n_jobs = -1
        )

        grid_search.fit(X_train,y_train)

        best_model = grid_search.best_estimator_ 
        best_params = grid_search.best_params_ 
        logging.info(f"Mejores hiperparámetros encontrados: {best_params}")

        # Predicciones de probabilidad en el conjunto de prueba 
        y_probs = best_model.predict_proba(X_test)[:, 1]
        roc_auc = roc_auc_score(y_test,y_probs)
        logging.info(f"ROC-AUC Score en test: {roc_auc:.4f}")

        # Calculo de recall para los umbrales posibles
        precision, recall, thresholds = precision_recall_curve(y_test, y_probs)
        logging.info(f"Curva Precision-Recall calculada exitosamente.")

        # Calculo del score F2
        f2_score = (5 * precision * recall) / (4 * precision + recall + 1e-10)

        # Umbral que maximiza el sccore F2
        optimal_idx = np.argmax(f2_score)
        optimal_threshold = thresholds[optimal_idx] 
        logging.info(f"Umbral óptimo: {optimal_threshold:.4f}")
        
        #Aplicación del umbral optimo 
        y_pred_optimal = (y_probs > optimal_threshold).astype(int)

        # Reporte de rendimiento:
        print("\n--- REPORTE DE RENDIMIENTO (UMBRAL ÓPTIMO) ---")
        print(f"ROC-AUC Score: {roc_auc:.4f}")
        print(f"Umbral seleccionado: {optimal_threshold:.4f}")
        print("\nReporte de Clasificación:")
        print(classification_report(y_test, y_pred_optimal))
        
        # Matriz de confusion
        cm = confusion_matrix(y_test, y_pred_optimal)
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='coolwarm', cbar=True)
        plt.title(f'Matriz de Confusión Clínico (Threshold={optimal_threshold:.2f})')
        plt.ylabel('Valor Real (0=Sano, 1=SAE)')
        plt.xlabel('Predicción del Modelo')
        plt.show()

        # Guardar el modelo para MLOps
        model_path = 'clinical_xgboost_pipeline.pkl'
        joblib.dump(best_model, model_path)
        logging.info(f"Pipeline serializado y guardado exitosamente en: {model_path}")
        
        return best_model, optimal_threshold

        
    except Exception as e:
        logging.error(f"Error en el entrenamiento del modelo: {e}")
        raise

    return None


if __name__ == "__main__":
    data_eng = __import__('03_data_engineering')
    X_train, X_test, y_train, y_test, preprocessor = data_eng.run_engineering_pipeline()
    pipeline_final, threshold = train_and_evaluate_model(X_train, X_test, y_train, y_test, preprocessor)
    print(f"\n Modelo en memoria y listo para auditoría SHAP (Umbral: {threshold:.4f})")    
    

