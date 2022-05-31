import numpy as np
from layer import FullConnectedLayer
from relu import ReLULayer
from softmax import SoftMaxLayer
from sigmoid import SigmoidLayer
class ClassificationNeuralNetwork:
    def __init__(self, input_dim: int, hidden_dims: list[int], output_dim: int, learning_rate: float):
        self.learning_rate = learning_rate
        self.layers = [
            FullConnectedLayer(input_dim, hidden_dims[0]),
            FullConnectedLayer(hidden_dims[0], hidden_dims[1]),
            FullConnectedLayer(hidden_dims[1], hidden_dims[2]),
            FullConnectedLayer(hidden_dims[2], output_dim),
        ]
        self.actives = [
            ReLULayer(hidden_dims[0]),
            ReLULayer(hidden_dims[1]),
            ReLULayer(hidden_dims[2]),
        ]
        self.softmax = SoftMaxLayer(output_dim)

    def forward(self, input: np.ndarray) -> np.ndarray:
        temp = self.layers[0].forward(input)
        for i in range(3):
            temp = self.actives[i].forward(temp)
            temp = self.layers[i + 1].forward(temp)
        temp = self.softmax.forward(temp)
        return temp

    def backward(self, label):
        grad = self.softmax.backward(label)
        for i in range(3):
            grad = self.layers[3 - i].backward(grad)
            grad = self.actives[2 - i].backward(grad)
        self.layers[0].backward(grad)

    def update(self):
        for i in range(3):
            self.layers[i].update(self.learning_rate)

    def train(self, data, label):
        self.forward(data)
        print(self.softmax.calculate_loss(label))
        self.backward(label)
        self.update()

    def predict(self, data):
        return self.forward(data)


def sme_loss(predict, real):
    return np.sum(np.power((predict - real), 2)) / np.shape(predict)[0]

class RegressNeuralNetwork:
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, learning_rate: float):
        self.learning_rate = learning_rate
        self.first = FullConnectedLayer(input_dim, hidden_dim)
        self.middle = SigmoidLayer(hidden_dim)
        self.last = FullConnectedLayer(hidden_dim, output_dim)

    def forward(self, input):
        temp = self.first.forward(input)
        temp = self.middle.forward(temp)
        return self.last.forward(temp)

    def backward(self, predict, real):
        grad = predict - real
        grad = self.last.backward(grad)
        grad = self.middle.backward(grad)
        self.first.backward(grad)

    def update(self):
        self.first.update(self.learning_rate)
        self.last.update(self.learning_rate)

    def train(self, data, label):
        predict = self.forward(data)
        print(predict, sme_loss(predict, label))
        self.backward(predict, label)
        self.update()