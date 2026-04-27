import torch
import torch.nn as nn

class ClinicalNeuralNetwork(nn.Module):
    """Red neuronal profunda para predicción de toxicidad clínica."""
    def __init__(self, input_dim):
        super(ClinicalNeuralNetwork, self).__init__()
        # Capas densas para capturar patrones altamente no lineales
        self.layer_1 = nn.Linear(input_dim, 32)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2) # Previene el sobreajuste
        self.layer_2 = nn.Linear(32, 16)
        self.output_layer = nn.Linear(16, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.layer_1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.layer_2(x)
        x = self.relu(x)
        x = self.output_layer(x)
        return self.sigmoid(x) # Retorna probabilidad entre 0 y 1