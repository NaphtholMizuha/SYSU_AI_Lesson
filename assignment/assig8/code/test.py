import numpy as np

def maj(x: np.ndarray):
    counts = np.bincount(x)
    majs = np.argwhere(counts == np.max(counts)).flatten()
    return np.random.choice(majs)

def dist(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.sqrt(np.sum(np.power(x - y, 2), axis=1))

def fetch_knn(x_train, test, k):
    dists = dist(x_train, test)
    print(dists)
    selected = dists.argpartition(k)[:k]
    print(f'{selected} selected with dist\n{dists[selected]}')
    return selected

def predict_unit(test, x_train, y_train, k):
        sample_indices = fetch_knn(x_train, test, k)
        sample_y = y_train[sample_indices]
        return np.argmax(np.bincount(sample_y))

def predict(x_train, x_test, y_train, k):
    return np.apply_along_axis(predict_unit, 1, x_test, x_train, y_train, k)


if __name__ == '__main__':
    x = np.array([1, 1, 4, 5, 1, 4, 4])
    for i in range(10):
        print(maj(x))
