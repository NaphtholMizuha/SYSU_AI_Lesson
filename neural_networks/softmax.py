import numpy as np
class SoftMaxLayer:
    def __init__(self, dim):
        self.dim = dim
        self.output = np.empty(dim)

    def forward(self, input):
        input_max = np.max(input, axis=1, keepdims=True)
        input_exp = np.exp(input - input_max)
        self.output = input_exp / np.sum(input_exp, axis=1, keepdims=True)
        return self.output

    def calculate_loss(self, label):
        return -np.sum((np.log(self.output) * label) / self.dim)

    def backward(self, label):
        return (self.output - label) / self.dim