import torch
import torch.nn as nn
import torch.optim as optim
import site
import fasttext

"""class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init()
        self.fc = nn.Linear(2, 1)

    def forward(self, x):
        return self.fc(x)

model = SimpleNN()

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
print("hello, world")"""
print(site.getsitepackages())
