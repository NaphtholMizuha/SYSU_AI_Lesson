import numpy as np
from scipy.special import expit as sigmoid

class SigmoidLayer:
    def __init__(self, dim: int):
        self.dim = dim
        self.output = None

    def forward(self, input: np.ndarray):
        self.output = sigmoid(input)
        return self.output

    def backward(self, grad: np.ndarray):
        return grad * self.output * (1 - self.output)