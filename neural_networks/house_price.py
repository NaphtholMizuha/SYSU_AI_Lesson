from neural_network import RegressNeuralNetwork, sme_loss
import numpy as np

def normalize(x):
    return (x - np.max(x, axis=0, keepdims=True)) / (np.min(x, axis=0, keepdims=True) - np.max(x, axis=0, keepdims=True))

def fetch_data(path):
    a = np.genfromtxt(path, delimiter=',', unpack=True)
    x = np.vstack([a[0], a[1]]).T
    y = a[2]
    return normalize(x), normalize(y)

if __name__ == '__main__':
    train_x, train_y = fetch_data('data/regress_data2.csv')
    n = RegressNeuralNetwork(
        input_dim=2,
        hidden_dim=4,
        output_dim=1,
        learning_rate=0.01
    )

    for i in range(5):
        indices = np.random.choice(47, 10)
        data = train_x[indices]
        real = train_y[indices]
        n.train(data, real)


