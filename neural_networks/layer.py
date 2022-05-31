import numpy as np

class FullConnectedLayer:
    def __init__(self, input_dim: int, output_dim: int):
        self.grad_bias = None
        self.grad_weight = None
        self.bias = np.zeros((1, output_dim))
        self.input = None
        self.grad = None
        self.weight = np.random.randn(input_dim, output_dim) * np.sqrt(2.0 / (input_dim * output_dim))

    def forward(self, input: np.ndarray):
        self.input = input
        return np.dot(input, self.weight) + self.bias

    def backward(self, grad_higher: np.ndarray):
        self.grad_weight = np.dot(self.input.T, grad_higher)
        self.grad_bias = np.sum(grad_higher, axis=0, keepdims=True)

        return np.dot(grad_higher, self.weight.T)

    def update(self, learning_rate):
        self.weight = np.subtract(self.weight, learning_rate * self.grad_weight)
        self.bias = np.subtract(self.bias, learning_rate * self.grad_bias)