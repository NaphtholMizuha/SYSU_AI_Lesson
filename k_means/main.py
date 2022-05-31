from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score

import figure
from parse import parse
import numpy as np

def dist(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.sqrt(np.sum(np.power(x - y, 2), axis=1))

def calc_min_d(centroids: np.ndarray, x: np.ndarray):
    dists = dist(centroids, x)
    return np.power(np.min(dists), 2)

def match_best_centroids(centroids: np.ndarray, x: np.ndarray):
    dists = dist(centroids, x)
    return np.argmin(dists)

def renew_centroids(x: np.ndarray, clusters: np.ndarray, k: int):
    new_centroids = []
    for i in range(k):
        indices = np.argwhere(clusters == i).flatten()
        x_cluster = x[indices, :]
        new_centroid = np.sum(x_cluster, axis=0) / np.size(x_cluster, axis=0)
        new_centroids.append(new_centroid)
    return np.array(new_centroids)

def init_standard(x: np.ndarray, k: int):
    x_col, x_row = x.shape
    return np.random.choice(np.arange(x_col), size=k, replace=False)

def init_plusplus(x: np.ndarray, k: int):
    x_row, x_col = x.shape
    first = np.random.choice(np.arange(x_row))
    selected = np.array([first])

    for i in range(k-1):
        remained_indices = np.where(np.arange(x_row) != selected.any())[0]
        d_x = np.apply_along_axis(calc_min_d, 1, x[remained_indices, :], x[selected, :])
        new_centroid = np.random.choice(remained_indices, p=d_x/np.sum(d_x))
        selected = np.append(selected, new_centroid)

    return selected

def k_means(x: np.ndarray, k: int, plusplus: bool):
    if plusplus:
        centroids_indices = init_plusplus(x, k)
    else:
        centroids_indices = init_standard(x, k)

    centroids = x[centroids_indices, :]
    init_centroids = centroids
    while True:
        clusters = np.apply_along_axis(match_best_centroids, 1, x, centroids)
        new_centroids = renew_centroids(x, clusters, k)
        if np.all(dist(centroids, new_centroids)) < 0.00001:
            return init_centroids, centroids, clusters
        else:
            centroids = new_centroids

if __name__ == '__main__':
    data, labels = parse('data.txt')
    vectorizer = CountVectorizer()
    train = vectorizer.fit_transform(data).toarray()
    init_centroids, centroids, cluster = k_means(train, 6, False)
    print(train.shape)
    print(centroids.shape)
    train_ = np.vstack((train, centroids))
    print(train_.shape)

    temp = TSNE().fit_transform(train_)
    centroids_show = temp[-6:]
    train_show = temp[:-6]
    score = silhouette_score(train, cluster, sample_size=cluster.size)
    print(f' score: {score}')
    figure.draw_result(train_show, cluster, centroids_show)


