import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import logging 


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', 
    filename = 'clinical_pipeline.log',
    filemode = 'a'
) 

sns.set_theme(style='darkgrid', palette = 'muted')

def run_eda_pipeline(data_path: str = "../data/raw/clinical_data_raw.csv"):
    """Carga de datos y ejecución de análisis exploratorio de datos"""
    
    # Carga de datos con bloque try-except 
    try:
        df = pd.read_csv(data_path)
        logging.info(f"Carga correcta de datos, número de registros = {df.shape[0]}")
        print("Resumen clínico del dataset:")
        print(f"Información de datos:\n{df.info()}")
        print(f"\nResumen estadístico de datos:\n{df.describe()}")
        null_counts = df.isnull().sum()
        print(f"\nValores nulos encontrados:\n{null_counts[null_counts > 0]}")
        print("\nBalance de clases objetivo")
        print(df['severe_adverse_event'].value_counts(normalize=True).round(3) * 100)


        # Visualiaciones 
        fig, axes = plt.subplots(2, 2, figsize=(15, 8))
        ax1, ax2, ax3, ax4 = axes.flatten()
        fig.suptitle('Análisis exploratorio de riesgo clínico', fontsize=16, fontweight='bold')

        # Distribución de la variable target 
        sns.countplot(
            data = df, 
            x = "severe_adverse_event", 
            palette = 'viridis', 
            ax = ax1, 
            hue = 'severe_adverse_event'
        )
        ax1.set_title('Distribución de eventos adversos', fontsize = 12, fontweight='bold')
        ax1.set_xlabel('Pacientes', fontsize = 12, fontweight = 'bold')

        # comparación de enzima vs target 
        sns.boxplot(
            data= df, 
            x = 'severe_adverse_event', 
            y = 'alt_enzyme_level', 
            palette = 'viridis', 
            ax=ax2,
            hue = 'severe_adverse_event'
        )
        ax2.set_title('Enzima ALT vsEvento Adverso Grave', fontsize = 12, fontweight='bold')
        ax2.set_xlabel('Evento Adverso Grave', fontsize = 12, fontweight = 'bold')
        ax2.set_ylabel('Enzima ALT', fontsize = 12, fontweight = 'bold')

        # Correlación de varialbes numéricas 
        num_cols = df.select_dtypes(include ='number').drop(columns = ['patient_id'], errors = 'ignore')
        correlation_matrix = num_cols.corr(method = 'pearson')
        sns.heatmap(
            correlation_matrix,
            annot = True, 
            cmap = 'coolwarm', 
            fmt = '.2f', 
            linewidths = 0.5, 
            ax = ax3
        )
        ax3.set_title('Mapa de correlación', fontsize = 12, fontweight='bold')


        # Incidencias de SAE por brazo de tratamiento 
        sns.barplot(
            data = df, 
            x = 'treatment_arm', 
            y = 'severe_adverse_event', 
            palette = 'viridis', 
            ax = ax4,
            errorbar = None, 
            hue = 'severe_adverse_event'
        )
        ax4.set_title('Incidencia de SAE por brazo de tratamiento', fontsize = 12, fontweight='bold')
        ax4.set_xlabel('Brazo de tratamiento', fontsize = 12, fontweight='bold')
        ax4.set_ylabel('Incidencia de SAE', fontsize = 12, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        logging.info("EDA completado con éxito.")
        
        
    except Exception as e: 
        logging.exception(f"Error en la ejecución del pipeline EDA: {e}")
        print(f"Ocurrió un error. Revisa el archivo 'clinical_pipeline.log' para más detalles.")

if __name__ == '__main__':
    run_eda_pipeline()