import pandas as pd
import numpy as np
import logging
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Configuración de logging
logging.basicConfig(
    filename="clinical_transformer.log",
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S', 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filemode='w'
)

def calculate_vif(X_transformed, feature_names):
    """Calcula VIF para determinar multicolinealidad"""
    try:
        vif_data = pd.DataFrame()
        vif_data['Features'] = feature_names 
        vif_data['VIF'] = [
            variance_inflation_factor(X_transformed, i) for i in range(X_transformed.shape[1])
        ]
        logging.info("VIF calculado correctamente")

        # Evaluación de VIF
        high_vif = vif_data[vif_data['VIF'] >= 5]
        if not high_vif.empty:
            problematic = high_vif['Features'].tolist()
            logging.error(f"FALLO DE VIF: Multicolinealidad detectada en: {problematic}")
            raise ValueError(f"Ejecución abortada: VIF >= 5 en {problematic}")
            
        logging.info("Prueba VIF exitosa: Todas las variables tienen un VIF menor a 5.")
        return vif_data.sort_values(by="VIF", ascending=False)

    except Exception as e:
        logging.error(f"Error en el proceso de VIF: {e}")
        raise e 

def run_engineering_pipeline(data_path: str = '../../data/raw/clinical_data_raw.csv'):
    logging.info(f"Iniciando el pipeline de ingeniería de datos... {data_path}")
    try:
        df = pd.read_csv(data_path)

        # Separación de columnas X y y
        X = df.drop(columns=['patient_id', 'severe_adverse_event']) #Features
        y = df['severe_adverse_event'] # Target

        # Separación de conjunto de entrenamiento y prueba 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21, stratify=y)
        logging.info(f"Datos divididos con éxito, registros de entrenamiento: {len(X_train)}")

        # Definición de grupos de variables
        num_columns = X.select_dtypes(include='number').columns.tolist()
        cat_columns = X.select_dtypes(include=['object', 'string']).columns.tolist()

        # Pipeline numérico
        num_pipeline = Pipeline( steps =[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()) # Estandaraziación de variables numéricas para comparar diferentes rangos de valores.
        ])

        # Pipeline categórico
        cat_pipeline = Pipeline(steps =[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')) #drop = 'first' evita la multicolinealidad, evita inferir columnas a partir de otras. 
        ])

        # Column Transformer
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', num_pipeline, num_columns),
                ('cat', cat_pipeline, cat_columns)
            ],
            remainder='drop',
            n_jobs=-1
        )

        # Fit y Transform en entrenamiento
        X_train_processed = preprocessor.fit_transform(X_train)
        logging.info("Feature engineering (fit_transform) completado en entrenamiento")

        # Obtener nombres de columnas transformadas
        cat_encoder = preprocessor.named_transformers_["cat"].named_steps["encoder"]
        cat_features_names = cat_encoder.get_feature_names_out(cat_columns)
        all_features_names = num_columns + list(cat_features_names)
        
        # Calcular VIF
        vif_results = calculate_vif(X_train_processed, all_features_names)

        print("\n--- REPORTE DE INGENIERÍA DE CARACTERÍSTICAS ---")
        print(vif_results.to_string(index=False))
        
        logging.info("Preprocesamiento finalizado con éxito.")

        print("Proceso concluido de forma exitosa.")
        
        return X_train, X_test, y_train, y_test, preprocessor

    except Exception as e:
        logging.error(f"Error crítico en el pipeline: {e}")
        print(f"Error detectado: {e}")
        raise

if __name__ == "__main__":
    X_train_proc, X_test, y_train, y_test, preprocessor = run_engineering_pipeline()
