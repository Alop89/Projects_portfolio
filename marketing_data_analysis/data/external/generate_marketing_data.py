import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración de aleatoriedad para reproducibilidad
np.random.seed(42)

# 1. Definición de parámetros base
fechas = [datetime(2026, 5, 20) + timedelta(days=i) for i in range(32)]
campanas = ['CAMP_PRO_AI_2026', 'CAMP_B2B_TALENT', 'CAMP_RECRUIT_GROWTH']

data_email = []
data_ads = []

# 2. Generación de datos históricos con lógica de negocio
for fecha in fechas:
    for camp in campanas:
        # --- CANAL: EMAIL ---
        enviados = int(np.random.normal(15000, 2000))
        # Tasa de apertura normal entre 18% y 25%
        tasa_apertura = np.random.uniform(0.18, 0.25)
        abiertos = int(enviados * tasa_apertura)
        # Tasa de clics normal entre 2% y 5% sobre abiertos
        tasa_clics_em = np.random.uniform(0.02, 0.05)
        clics_em = int(abiertos * tasa_clics_em)
        bounces = int(enviados * np.random.uniform(0.01, 0.03))
        
        # --- CANAL: LINKEDIN ADS ---
        impresiones = int(np.random.normal(50000, 5000))
        # CTR normal entre 0.8% y 1.5%
        ctr_ads = np.random.uniform(0.008, 0.015)
        clics_ads = int(impresiones * ctr_ads)
        # Costo por clic promedio de $2.5 USD
        gasto = round(clics_ads * np.random.uniform(2.2, 2.8), 2)
        # Conversiones normales (10% al 15% de los clics)
        conversiones = int(clics_ads * np.random.uniform(0.10, 0.15))

        # ─── INYECCIÓN DE ANOMALÍAS Y RUIDO (Para el reto de análisis) ───
        # Anomalía 1: El 5 de Junio falló el tracking de clics en la campaña B2B de Ads (Enlace roto)
        if fecha == datetime(2026, 6, 5) and camp == 'CAMP_B2B_TALENT':
            clics_ads = int(clics_ads * 0.05)
            conversiones = 0
            
        # Anomalía 2: El 15 de Junio hubo un problema con el servidor de correos (Altos Bounces)
        if fecha == datetime(2026, 6, 15):
            bounces = int(enviados * 0.45) # 45% de rebote
            clics_em = int(clics_em * 0.1)

        # Inyección de algunos valores nulos aleatorios para limpieza (Data Integrity)
        bounces = None if np.random.rand() < 0.03 else bounces
        gasto = None if np.random.rand() < 0.02 else gasto

        # Guardar registros
        data_email.append({
            'campaign_id': camp,
            'date': fecha.strftime('%Y-%m-%d'),
            'emails_sent': enviados,
            'emails_opened': abiertos,
            'emails_clicked': clics_em,
            'bounces': bounces
        })

        data_ads.append({
            'campaign_id': camp,
            'date': fecha.strftime('%Y-%m-%d'),
            'impressions': impresiones,
            'clicks': clics_ads,
            'spend_usd': gasto,
            'conversions': conversiones
        })

# 3. Crear DataFrames y exportar a CSV
df_email = pd.DataFrame(data_email)
df_ads = pd.DataFrame(data_ads)

df_email.to_csv('../raw/email_campaigns_log.csv', index=False)
df_ads.to_csv('../raw/linkedin_ads_perf.csv', index=False)

print("¡Datasets generados con éxito!")
print(f"Registros de Email: {len(df_email)} | Registros de Ads: {len(df_ads)}")