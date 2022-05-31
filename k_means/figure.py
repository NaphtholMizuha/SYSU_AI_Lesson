import matplotlib.pyplot as plt
import numpy as np
def draw_init_state(train, init_centroids):
    plt.scatter(train[:, 0], train[:, 1], c='gray', marker='1', s=20)
    plt.scatter(init_centroids[:, 0], init_centroids[:, 1], marker='x', c='black', s=100)
    plt.title('K-means First Centroids')
    plt.savefig('init++.pdf')
    plt.show()

def draw_result(train, cluster, centroids):
    colors = ['#ff1500', '#1C86EE', '#EEC900', '#3CB371', '#FF8C00', '#9370DB']
    for index in range(6):
        x = train[np.where(cluster == index), 0]
        y = train[np.where(cluster == index), 1]
        plt.scatter(x, y, c=colors[index], marker='1', s=20)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='black', s=100)
    plt.title('Results')
    plt.savefig('result++.pdf')
    plt.show()