# Librerias 
import pandas as pd
import numpy as np
import joblib
import sys 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, precision_recall_curve
from sklearn.metrics import ConfusionMatrixDisplay


# Caarga de datos 
try:
    path = "../data/raw/clinical_trial_data.csv"
    df = pd.read_csv(path)
    print(df.sample(10))
except:
    print("Error, datos no encontrados en la ruta ")
    sys.exit()


# Ingeniería de datos 

X = df.drop(['Dropped_Out','Patient_ID'], axis = 1)
y = df['Dropped_Out']

# Separación y entrenamiento 

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state =42, stratify = y) 
print(f"Total de paciente, set de entrenamiento {len(X_train)}, set de prueba {len(X_test)}")

# Data engineering 
numeric_c = ['Age', 'BMI', 'Systolic_BP', 'Glucose_Level']
categorical_c = ['Gender', 'Treatment_Arm']

preprocessor = ColumnTransformer(
    transformers= [
        ('num', StandardScaler(), numeric_c),
        ('cat', OneHotEncoder(drop = 'first',sparse_output = False), categorical_c)
    ], 
    remainder= 'passthrough'
)


# Pipeline 

pipeline = Pipeline(
    steps =[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(class_weight= 'balanced', random_state= 42, max_iter=1000))
    ]
)

# Cross validation
cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state= 42)

param_grid = {
    'classifier__C':[0.01,0.1,1,10],
    
}

grid_search = GridSearchCV(pipeline, param_grid, cv = cv_strategy, scoring= 'roc_auc', n_jobs= -1)

grid_search.fit(X_train, Y_train)

best_estimator = grid_search.best_estimator_
best_params = grid_search.best_params_


print(f"Los mejores hiperparámetros para el modelo de regresión logistica son \n{best_params}")


# Optimización del umbral clínico 

y_scores = best_model.predict_proba(X_test)[:,1]

precisions, recalls, thresholds = precision_recall_curve(Y_test, y_scores)

f2_scores = (5 * precisions[:-1] * recalls[:-1]) / ((4 * precisions[:-1]) + recalls[:-1])

optimal_idx = np.nanargmax(f2_scores)
optimal_thresholds = thresholds[optimal_idx]

print(f"El umbral óptima calculado fue de = {optimal_thresholds:.3f}")


# Evaluación y persistencia 

y_pred_custom = (y_scores >= optimal_thresholds).astype(int)

print("\nREPORTE DE CLASIFICACIÓN (umbral ajustado):")
print(classification_report(Y_test, y_pred_custom))


roc_auc = roc_auc_score(Y_test, y_scores)
print(f"ROC-AUC Score: {roc_auc:.3f}")

print("\n Matriz de confusión")
cm = confusion_matrix(Y_test, y_pred_custom)
print(f"Verdaderos Negativos (Terminan y acertamos): {cm[0][0]}")
print(f"Falsos Positivos (Falsa Alarma): {cm[0][1]}")
print(f"Falsos Negativos (PELIGRO - Abandonó y no avisamos): {cm[1][0]}")
print(f"Verdaderos Positivos (Abandono detectado a tiempo): {cm[1][1]}")


# Visualización de la matriz de confusión

ConfusionMatrixDisplay.from_predictions(Y_test, y_pred_custom, 
                                        display_labels=['No Abandonó', 'Abandonó'],
                                        cmap='magma')
plt.title('Matriz de Confusión')
plt.show()


