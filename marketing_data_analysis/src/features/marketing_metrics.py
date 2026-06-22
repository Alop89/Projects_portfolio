import os
import pandas as pd
import numpy as np

def ejecutar_eda_marketing():
    # 1. Loading master dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        master_path = os.path.join(script_dir, '..', '..', 'data', 'processed', 'marketing_master_dataset.csv')
        df = pd.read_csv(master_path)
        df['date'] = pd.to_datetime(df['date'])
    except FileNotFoundError as e:
        print(f"Error: no data was found. {e}")
        return None
    
    print("="*60)
    print("      STRATEGIC EDA: LINKEDIN OWNED MEDIA AGENCY")
    print("="*60)
    
    # 2. KPI calculations
    df['email_open_rate'] = np.where(df['emails_sent'] > 0, df['emails_opened'] / df['emails_sent'], 0)
    df['email_ctr'] = np.where(df['emails_opened'] > 0, df['emails_clicked'] / df['emails_opened'], 0)
    df['ads_ctr'] = np.where(df['impressions'] > 0, df['clicks'] / df['impressions'], 0)
    df['ads_conversion_rate'] = np.where(df['clicks'] > 0, df['conversions'] / df['clicks'], 0)
    df['cpc'] = np.where(df['clicks'] > 0, df['spend_usd'] / df['clicks'], 0)

    # 3. Statistical summary per campaign
    print("\n--- 1. Average performance by campaign ---")
    resumen_campanas = df.groupby('campaign_id').agg({
        'email_open_rate': 'mean',
        'email_ctr': 'mean',
        'ads_ctr': 'mean',
        'ads_conversion_rate': 'mean',
        'spend_usd': 'sum',
        'conversions': 'sum'
    }).round(4)
    print(resumen_campanas)

    # 4. Seasonal effect
    print("\n--- 2. Seasonal effect ---")
    df['day_of_week'] = df['date'].dt.day_name()
    orden_dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    resumen_semanal = df.groupby('day_of_week').agg({
        'clicks': 'mean',
        'conversions': 'mean'
    }).reindex(orden_dias).round(1)
    print(resumen_semanal)

    # 5. Anomalies detection using sigma rule
    print("\n--- 3. Anomalies detection ---")
    for canal, metrica in [('LinkedIn Ads', 'ads_ctr'), ('Email', 'email_open_rate')]:
        mean = df[metrica].mean()
        std = df[metrica].std()
        # We search for days that are more than 2 standard deviations away from the mean (downward)
        limite_inferior = mean - (2 * std)
        
        anomalies = df[df[metrica] < limite_inferior]
        print(f"\n   -> Chanel {canal} (Searching for drastic drops in {metrica}):")
        if not anomalies.empty:
            for idx, row in anomalies.iterrows():
                print(f"      [ALERT] Date: {row['date'].strftime('%Y-%m-%d')} | Campaign: {row['campaign_id']} | Value: {round(row[metrica], 4)} (Historical Average: {round(mean, 4)})")
        else:
            print("      [OK] No obvious anomalies were detected with this criterion.")
            
    # 6. Correlation matrix (to understand growth drivers)
    print("\n--- 4. Correlation matrix (LinkedIn Ads) ---")
    columnas_corr = ['impressions', 'clicks', 'spend_usd', 'conversions']
    matriz_corr = df[columnas_corr].corr().round(2)
    print(matriz_corr)
    
    print("="*60)

if __name__ == "__main__":
    ejecutar_eda_marketing()