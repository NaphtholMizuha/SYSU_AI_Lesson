import numpy as np

from relu import ReLULayer
from neural_network import ClassificationNeuralNetwork
from layer import FullConnectedLayer
from softmax import SoftMaxLayer

def test_layer():
    l = FullConnectedLayer(3, 2, 1)
    l.weight = np.array([
        [1, 1,], [4, 5], [1, 4],
    ])
    test_layer_forward(l)
    test_layer_backward(l)

def test_layer_forward(layer):
    ipt = np.arange(9).reshape((3,3))
    weight = np.array([
        [1, 1, ], [4, 5], [1, 4],
    ])
    result = layer.forward(ipt)
    assert result.all() == np.dot(ipt, weight).all()

def test_layer_backward(layer):
    grad_y = np.array([1,9,1,9,8,1]).reshape([3,2])
    grad_x = layer.backward(grad_y)
    print(layer.input.T)
    print(grad_y)
    print(layer.grad_bias)

def test_active():
    al = ReLULayer(dim=6)
    arr = np.array([-1, 1, 4, -5, 1, -4])
    assert np.all(al.forward(arr) == np.array([0,1,4,0,1,0]))
    grad_y = np.array([3, 6, 4, 3, 6, 4])
    print(al.backward(grad_y))
    assert np.all(al.backward(grad_y) == np.array([0,6,4,0,6,0]))

def test_softmax():
    softmax = SoftMaxLayer(6)
    arr = np.array([[-1, 1, 4, -5, 1, -4],[1,9,1,9,8,1]])
    print(softmax.forward(arr))

if __name__ == '__main__':
    test_layer()
    test_active()
    test_softmax()