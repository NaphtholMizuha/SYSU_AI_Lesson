import numpy as np
from parse import fetch_parsed_data
from neural_network import ClassificationNeuralNetwork

if __name__ == '__main__':
    train_img, train_label, test_img, test_label = fetch_parsed_data()
    train_img = train_img / 255
    nn = ClassificationNeuralNetwork(
        input_dim=28 * 28,
        hidden_dims=[256,128,64],
        output_dim=10,
        learning_rate=0.01
    )

    for i in range(10000):
        index = np.random.choice(60000, 100)
        data = train_img[index]
        label = train_label[index]
        nn.train(data, label)

    predict = nn.predict(test_img)
    predict = np.argmax(predict, axis=1, keepdims=True)
    real = np.argmax(test_label, axis=1, keepdims=True)
    matches = np.equal(predict, real)
    print(f'Accuracy: {np.sum(matches) / np.size(matches)}')

    hand = np.load('data/hand_written.npy')
    predict = nn.predict(hand)
    print(np.argmax(predict, axis=1, keepdims=True))







