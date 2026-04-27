import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import joblib
import logging
import os
from sklearn.model_selection import train_test_split


logging.basicConfig(
    level =logging.INFO, 
    format ="%(asctime)s - %(levelname)s - %(message)s",
    datefmt ="%Y-%m-%d %H:%M:%S",
    filename ="train_pytorch.log",
    filemode = 'w'    
    )


try:
    from pytorch_model import ClinicalNeuralNetwork
    logging.info("PyTorch, modelo importado de forma exitosa")
except ModuleNotFoundError:
    from src.models.pytorch_model import ClinicalNeuralNetwork  
    logging.info("Modelo importado usando ruta absoluta")

def train_deep_learning_model():
    """
    Función principal para entrenar el modelo de deep learning
    """

    # Ruta para carga de datos
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    data_path = os.path.join(base_dir, 'data', 'raw', 'clinical_data_raw.csv')
    xgb_model_path = os.path.join(base_dir, 'src', 'models', 'clinical_xgboost_pipeline.pkl')


    try:
        # Carga de datos en estructura DataFrame
        df = pd.read_csv(data_path)
        X = df.drop(columns =['patient_id', 'severe_adverse_event'])
        y = df['severe_adverse_event']

        # Separación de datos en sets de entrenamiento y prueba 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 21, stratify= y)

        # Extracción del pipeline 
        xgb_pipeline = joblib.load(xgb_model_path)
        preprocessor = xgb_pipeline.named_steps['preprocessor']

        # Conversión de datos con preprocesador
        X_train_proc = preprocessor.transform(X_train)

        # Conversor a tensores PyTorch
        X_train_tensor = torch.FloatTensor(X_train_proc)
        y_train_tensor = torch.FloatTensor(y_train.values.copy()).view(-1, 1)

        # Red neuronal 
        input_dim = X_train_tensor.shape[1]
        model = ClinicalNeuralNetwork(input_dim)

        # Función de pérdida para clasificación binaria
        criterion = nn.BCELoss()
        optimizer = optim.Adam(model.parameters(), lr= 0.005)

        # Bucle de entrenamiento
        epochs = 150
        logging.info("Comenzando entrenamiento del modelo de deep learning")

        model.train()

        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X_train_tensor)
            loss = criterion(outputs, y_train_tensor)
            loss.backward()
            optimizer.step()

            if (epoch+1) %30 ==0:
                logging.info(f'Epoch [{epoch}/{epochs}], Loss: {loss.item():.4f}')
        
        save_path = os.path.join(base_dir, 'src', 'models', 'clinical_pytorch_model.pt')
        torch.save(model.state_dict(), save_path)
        logging.info(f"Pesos de la red neuronal guardados en: {save_path}")

    except Exception as e:
        logging.error(f"Error durante el entrenamiento: {e}")
        raise 

    finally:
        logging.info("Proceso de entrenamiento finalizado")

if __name__ == '__main__':
    train_deep_learning_model()