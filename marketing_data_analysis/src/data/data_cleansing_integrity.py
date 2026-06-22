import os
import pandas as pd
import numpy as np

def cargar_y_limpiar_datos():
    # Get directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Data load
    print(" Loading data...")
    try:
        email_path = os.path.join(script_dir, '..', '..', 'data', 'raw', 'email_campaigns_log.csv')
        ads_path = os.path.join(script_dir, '..', '..', 'data', 'raw', 'linkedin_ads_perf.csv')
        
        df_email = pd.read_csv(email_path)
        df_ads = pd.read_csv(ads_path)
    except FileNotFoundError as e:
        print(f"Error: no data were found. {e}")
        return None

    # 2. Cleaning channel: email

    df_email['bounces'] = df_email['bounces'].fillna(0).astype(int)



    # 3. Cleaning channel: LinkedIn Ads

    print(" Null data addressed...")
    

    df_ads['cpc_temp'] = df_ads['spend_usd'] / df_ads['clicks']
    cpc_promedio_por_campana = df_ads.groupby('campaign_id')['cpc_temp'].transform('mean')
    
  
    gasto_estimado = df_ads['clicks'] * cpc_promedio_por_campana
    df_ads['spend_usd'] = df_ads['spend_usd'].fillna(gasto_estimado).round(2)
    df_ads.drop(columns=['cpc_temp'], inplace=True)

        # Data format 
    df_ads['date'] = pd.to_datetime(df_ads['date']).dt.date
    df_email['date'] = pd.to_datetime(df_email['date']).dt.date

    # 4. JOINT both datasets 

    print(" Jointing the channels (Email + LinkedIn Ads)...")
    df_master = pd.merge(
        df_email, 
        df_ads, 
        on=['date', 'campaign_id'], 
        how='outer'
    )

    

   
    metricas_columnas = ['emails_sent', 'emails_opened', 'emails_clicked', 'bounces', 'impressions', 'clicks', 'spend_usd', 'conversions']
    df_master[metricas_columnas] = df_master[metricas_columnas].fillna(0)

    # 5. Quality controls
    print(" Running data quality checks...")
    
    # Regla 1: Los clics no pueden ser mayores que las aperturas en Email
    assert (df_master['emails_clicked'] <= df_master['emails_opened']).all(), "⚠️ Alerta: Clics de Email superan a las aperturas."
    
    # Regla 2: Los clics de Ads no pueden superar las impresiones
    assert (df_master['clicks'] <= df_master['impressions']).all(), "⚠️ Alerta: Clics de Ads superan a las impresiones."
    
    # Regla 3: No deben quedar valores nulos en el dataset final
    assert df_master.isnull().sum().sum() == 0, "⚠️ Alerta: Aún existen valores nulos en el dataset maestro."

    print(" ¡Control de calidad exitoso! Data limpia y verificada.")
    
    # 6. Exportar Dataset Maestro
    export_path = os.path.join(script_dir, '..', '..', 'data', 'processed', 'marketing_master_dataset.csv')
    df_master.to_csv(export_path, index=False)
    print(f"[SUCCESS] 'marketing_master_dataset.csv' saved at: {export_path}")
    
    return df_master

if __name__ == "__main__":
    df_limpio = cargar_y_limpiar_datos()
    print(df_limpio.head(5))