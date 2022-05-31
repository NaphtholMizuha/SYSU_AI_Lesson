import numpy as np

class ReLULayer:
    def __init__(self, dim: int):
        self.dim = dim
        self.input = None

    def forward(self, input: np.ndarray):
        self.input = input
        return np.maximum(input, 0)

    def backward(self, grad: np.ndarray):
        grad[self.input < 0] = 0
        return grad