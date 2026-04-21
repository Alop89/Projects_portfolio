import os 
import pandas as pd 
from sqlalchemy import create_engine
import logging 
from dotenv import load_dotenv

load_dotenv()


# Carga de datos de .env
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("NEON_PASSWORD")
DB_HOST = os.getenv("NEON_HOST")
DB_DB = os.getenv("NEON_DB")


# Creación de conexión a base de datos
DATABASE_URL = os.getenv("DATABASE_URL")


def process_and_upload(filepath):
    try:
        print(f"Inicio de proceso de ETL del archivo: {filepath}")
        logging.info(f"Inicio de proceso ETL para: {filepath}")

        # Carga de datos
        df = pd.read_csv(filepath)
        print(f"Archivo cargado correctamente, filas: {len(df)}")
        logging.info(f"Archivo cargado correctamente, filas: {len(df)}")

        # Transformación de datos
        df['Date'] = pd.to_datetime(df['Date'])
        
        if df.isnull().values.any():
            nulls = df.isnull().sum()
            print(f"Se detectaron valores nulos en el archivo :{nulls}")
            logging.info(f"Se detectaron valores nulos: {nulls}")
            # Imputación de dato
            df.fillna({
                'Quantity': 0, 
                'Total_Sales_USD': 0.0, 
            }, inplace = True)
        
        # Conexión a base de datos 
        engine = create_engine(DATABASE_URL)

        #Agregar datos nuevos 
        df.to_sql('medtech_sales_data', engine, if_exists='append', index=False)
        logging.info(f"Datos agregados correctamente a la tabla medtech_sales_data")
        print("Datos agregados correctamente a la tabla medtech_sales_data")

        # Marcar archivo como procesado 
        ruta_procesada = filepath + ".processed"
        os.rename(filepath, ruta_procesada)
        logging.info(f"Archivo movido a procesados: {ruta_procesada}")
        print(f"Archivo renombrado como procesado: {ruta_procesada}")

        print(f"Proceso ETL completado para: {filepath}")
        logging.info(f"Proceso ETL completado para: {filepath}")

    except Exception as e:
        logging.error(f"Error procesando archivo {filepath}: {e}")
        print(f"Error procesando archivo {filepath}: {e}")
        

      
        
        
