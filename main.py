import torch
import torch.nn as nn
import torch.optim as optim

class(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc = nn.Linear(2,1)

    def forward(self, x):
        return self.fc
    
model = SimpleNN()

criterion = nn.MSELoss()
optimzer = optim.SGD(model.parameters(), lr = 0.01)