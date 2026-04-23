import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


try:
    path = "../../data/raw/clinical_trial_data.csv"
    df = pd.read_csv(path)  
    print("Datos cargados correctamente")
    print(f"Shape: {df.shape}")
except:
    print("Error, datos no encontrados en la ruta ")


# Ingeniería de datos 

X = df.drop(['Dropped_Out','Patient_ID'], axis = 1)
y = df['Dropped_Out']

# Separación y entrenamiento 

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state =42, stratify = y) 
print(f"Total de paciente, set de entrenamiento {len(X_train)}, set de prueba {len(X_test)}")

# Columnas numéricas y categóricas 

numeric_c = ['Age', 'BMI', 'Systolic_BP', 'Glucose_Level']
categorical_c = ['Gender', 'Treatment_Arm']

# Preprocesamiento

preprocessor = ColumnTransformer(
    transformers= [
        ('num', StandardScaler(), numeric_c),
        ('cat', OneHotEncoder(drop = 'first', sparse_output = False), categorical_c)
    ], 
    remainder = 'passthrough'
)

# Tratamiento para evitar la fuga de datos 

X_train_pp = preprocessor.fit_transform(X_train)

X_test_pp = preprocessor.fit(X_test)


# Extracción de columnas para explicación clínica 

cat_features_n = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_c)
all_features_n = numeric_c + list(cat_features_n)

X_train_f = pd.DataFrame(X_train_pp, columns = all_features_n, index= X_train.index)
X_test_f = pd.DataFrame(X_test_pp, columns = all_features_n, index = X_test.index)

# MLOPs readiness 

joblib.dump(preprocessor, 'clinical_preprocessor.pkl')
print("Datos de entrenamiento y prueba procesados correctamente\n")
print(X_train_f.head())
