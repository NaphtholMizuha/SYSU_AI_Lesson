from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from parse import parse
import numpy as np
import matplotlib.pyplot as plt

def maj(x: np.ndarray):
    counts = np.bincount(x)
    majs = np.argwhere(counts == np.max(counts)).flatten()
    # 多个众数时随机选择
    return np.random.choice(majs)

def dist(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    # Euclid距离
    return np.sqrt(np.sum(np.power(x - y, 2), axis=1))

def fetch_knn(x_train, test, k):
    dists = dist(x_train, test) # 计算距离
    return dists.argpartition(k)[:k] # 返回距离最小的k个

def predict_unit(test, x_train, y_train, k):
    # 获取knn的索引
    sample_indices = fetch_knn(x_train, test, k)
    # 通过索引获取标签
    sample_y = y_train[sample_indices]
    # 返回众数
    return maj(sample_y)

def predict(x_train, x_test, y_train, k):
    return np.apply_along_axis(predict_unit, 1, x_test, x_train, y_train, k)


if __name__ == '__main__':
    x, y = parse('data.txt')
    vectorizer = TfidfVectorizer()
    x_data = vectorizer.fit_transform(x).toarray()
    x_train = x_data[:1000, :]
    x_test = x_data[1000:,:]
    y_data = np.array(y)
    y_train = y_data[:1000]
    y_test = y_data[1000:]

    x_axis = []
    y_axis = []

    for i in range(10, 40, 2):
        y_predict = predict(x_train, x_test, y_train, k=i)
        eqs = np.equal(y_predict, y_test)
        accuracy = np.sum(eqs) / np.size(eqs)
        print(f'real result:\n{y_test}')
        print(f'predict result:\n{y_predict}')
        print(f'Accuracy: {accuracy}')
        x_axis.append(i)
        y_axis.append(accuracy)

    plt.plot(x_axis, y_axis)
    plt.savefig('10to40.pdf')
    plt.show()



