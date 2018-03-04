import torch
from torch import nn
from torch


class SAE(nn.Module):
    def __init__(self):
        super(SAE, self).__init__()
        self.avgp = nn.AvgPool2d(kernel_size=18, stride=1)
        self.fc1 = nn.Sequential([
            nn.Linear(20164, 2000),
            nn.Dropout(0.5)
        ])
        self.relu = nn.ReLU()
        self.fc2 = nn.Sequential([
            nn.Linear(2000, 2),
            nn.Dropout(0.5)
        ])

    def init_params(self):
        for m in self.modules():
        if isinstance(m, nn.Linear):
            nn.init.xavier_uniform(m.weight)
            nn.init.constant(m.bias, 0)

    def forward(input):
        # input Batch_size * 160 * 160 * 3channels
        # local recptive + L2 pooling
        x = torch.sqrt(self.avgp(torch.mul(input, input)))
        # local contrast normalization

        # change to one-dimension tensor
        x = x.view(20164, -1)
        # feed-forward neural network
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)

        return x
