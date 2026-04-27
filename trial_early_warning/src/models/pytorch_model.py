import torch
import torch.nn as nn

class ClinicalNeuralNetwork(nn.Module):
    """
    Red neuronal profunda para la predicción de toxicidad en ensayos clínicos
    """
    def __init__(self, input_dim):
        super(ClinicalNeuralNetwork, self).__init__()

        # Capa densa
        self.layer_1 = nn.Linear(input_dim, 32)
        self.layer_2 = nn.Linear(32, 16)
        self.output_layer = nn.Linear(16, 1)


        # Activación y regularización 
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.layer_1(x)
        x = self.relu(x)
        x = self.dropout(x)

        x = self.layer_2(x)
        x = self.relu(x)
        x = self.dropout(x)

        x = self.output_layer(x)

        return self.sigmoid(x)
    
    