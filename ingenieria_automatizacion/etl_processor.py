import os 
import pandas as pd 
from sqlalchemy import create_engine, text
import logging 
from dotenv import load_dotenv, find_dotenv

# Aseguramos que lea el archivo .env sin importar desde dónde se ejecute
load_dotenv(find_dotenv())

# Carga de datos de .env (Corregido a NEON_USER)
DB_USER = os.getenv("NEON_USER")
DB_PASS = os.getenv("NEON_PASSWORD")
DB_HOST = os.getenv("NEON_HOST")
DB_DB = os.getenv("NEON_DB")
DATABASE_URL = os.getenv("DATABASE_URL")


def process_and_upload(filepath):
    try:
        print(f"Inicio de proceso de ETL del archivo: {filepath}")
        logging.info(f"Inicio de proceso ETL para: {filepath}")

       
        df = pd.read_csv(filepath)
        print(f"Archivo cargado correctamente, filas: {len(df)}")
        logging.info(f"Archivo cargado correctamente, filas: {len(df)}")

       
        df['Date'] = pd.to_datetime(df['Date']).dt.date

        seg__map = {
        'Consumibles' : 'Consumible alto volumne', 
        'Quirúrgicos' : 'Equipo medico alto valor', 
        'Imagenología': 'Imagenología'
        }
        
        df['Business_unit'] = df['Product_Category'].map(seg__map)
        
        # Validar nulos de forma nativa en pandas
        if df.isna().any().any():
            nulls = df.isnull().sum().sum()
            print(f"Se detectaron valores nulos en el archivo: {nulls}")
            logging.info(f"Se detectaron valores nulos: {nulls}")
            
            # Imputación de datos
            df.fillna({
                'Quantity': 0, 
                'Total_Sales_USD': 0.0, 
            }, inplace=True)
            
        engine = create_engine(DATABASE_URL)

        print("Subiendo datos a la tabla de tránsito (staging_medtech)...")
        df.to_sql('staging_medtech', engine, if_exists='replace', index=False)
        
        print("Ejecutando Fusión (Upsert) con la tabla principal...")
        with engine.begin() as conn:
            query = text("""
                INSERT INTO "medtech_sales_data" (
                    "Order_ID", "Date", "Hospital_Type", "Region", "Product_Category", 
                    "Product_Name", "Quantity", "Unit_Price_USD", "Discount_Applied", 
                    "Total_Sales_USD", "Customer_Satisfaction", "Business_unit"
                )
                SELECT 
                    "Order_ID", "Date", "Hospital_Type", "Region", "Product_Category", 
                    "Product_Name", "Quantity", "Unit_Price_USD", "Discount_Applied", 
                    "Total_Sales_USD", "Customer_Satisfaction", "Business_unit"
                FROM "staging_medtech"
                ON CONFLICT ("Order_ID") 
                DO UPDATE SET 
                    "Hospital_Type" = EXCLUDED."Hospital_Type",
                    "Region" = EXCLUDED."Region",
                    "Product_Category" = EXCLUDED."Product_Category",
                    "Product_Name" = EXCLUDED."Product_Name",
                    "Quantity" = EXCLUDED."Quantity",
                    "Unit_Price_USD" = EXCLUDED."Unit_Price_USD",
                    "Discount_Applied" = EXCLUDED."Discount_Applied",
                    "Total_Sales_USD" = EXCLUDED."Total_Sales_USD",
                    "Customer_Satisfaction" = EXCLUDED."Customer_Satisfaction", 
                    "Business_unit" = EXCLUDED."Business_unit";
            """)
            conn.execute(query)

        logging.info("Datos agregados/actualizados correctamente en medtech_sales_data")
        print("Datos agregados/actualizados correctamente en medtech_sales_data")

        ruta_procesada = filepath + ".processed"
        os.rename(filepath, ruta_procesada)
        logging.info(f"Archivo movido a procesados: {ruta_procesada}")
        print(f"Archivo renombrado como procesado: {ruta_procesada}")

        print(f"✅ Proceso ETL completado para: {filepath}\n")
        logging.info(f"Proceso ETL completado para: {filepath}")

    except Exception as e:
        logging.error(f"Error procesando archivo {filepath}: {e}")
        print(f"❌ Error procesando archivo {filepath}: {e}")  
        
        
