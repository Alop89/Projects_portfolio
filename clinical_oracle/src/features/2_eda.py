import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_csv('../../data/raw/clinical_trial_data.csv')
print(f"Total de pacientes en el estudio: {len(df)}")

stay_ = df[df['Dropped_Out'] == 1].count() / len(df)
quit_ = df[df['Dropped_Out'] == 0].count() / len(df)

print(f"Proporción de pacientes que se quedaron {stay_}, \nPacientes que abandaron {quit_}")

df_numeric = df.drop("Patient_ID", axis = 1)

sns.pairplot(
    data = df_numeric
)


# Análisis de distribución 
sns.set_style("darkgrid")
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15,5))

sns.boxplot(
    data = df, 
    x = "Dropped_Out", 
    y= 'Age', 
    hue = 'Treatment_Arm', 
    ax = ax1,
    legend = False
)

sns.violinplot(
    data = df, 
    x = "Dropped_Out", 
    y= 'Systolic_BP', 
    hue = 'Treatment_Arm', 
    ax = ax2
)

ax1.set_title("Distribución de edad vs abandono del ensayo (por tratamiento)")
ax2.set_title("Distribución de presión sistólica vs abandono del ensayo (por tratamiento)")
ax2.legend(loc='upper right', bbox_to_anchor=(1.25, 0.5))
plt.show()


print("\n--- PRUEBAS ESTADÍSTICAS (HIPÓTESIS) ---")


bp_stayed = df[df['Dropped_Out'] == 0]['Systolic_BP']
bp_dropped = df[df['Dropped_Out'] == 1]['Systolic_BP']



t_stat, p_value = stats.ttest_ind(bp_stayed, bp_dropped)
print(f"T-Test Presión arterial vs abandono:")
print(f"P-Value: {p_value:.3f}")
if p_value < 0.05:
    print("Conclusión Clínica: Existe una diferencia estadísticamente significativa en la presión arterial de los pacientes que abandonan. ¡Es un biomarcador clave para nuestro modelo ML!\n")
else: 
    print("No hay difrencia estadística significativa")


contingency_table = pd.crosstab(df['Treatment_Arm'], df['Dropped_Out'])
chi2, p_val_chi, dof, expected = stats.chi2_contingency(contingency_table)

print(f"Chi-Cuadrada Tratamiento vs Abandono:")
print(f"P-Value: {p_val_chi:.5f}")
if p_val_chi < 0.05:
    print("Conclusión Clínica: El tipo de tratamiento (Placebo vs Drug_X) está fuertemente asociado con que el paciente termine el ensayo.")