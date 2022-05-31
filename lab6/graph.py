import numpy as np
import matplotlib.pyplot as plt

class NodeGraph:
    def __init__(self, path):
        self.pos, self.dimension = fetch_euclid(path)
        self.dist = np.zeros([self.dimension, self.dimension])
        for i in range(self.dimension):
            a = self.pos[i]
            for j in range(self.dimension):
                b = self.pos[j]
                self.dist[i][j] = np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def euclid_dist(self, i, j):
        return self.dist[i][j]

    def weight(self, state):
        result = self.euclid_dist(state[self.dimension - 1], state[0])
        for i in range(self.dimension - 1):
            result += self.euclid_dist(state[i], state[i + 1])
        return result

    def draw(self, state, title: str):
        x = [self.pos[item][0] for item in state]
        x.append(self.pos[state[0]][0])
        y = [self.pos[item][1] for item in state]
        y.append(self.pos[state[0]][1])
        plt.plot(x, y, 'o-')
        plt.title(title)
        title = title.split(' ')[0]
        plt.savefig(f'result/{title}.pdf')
        plt.show()

def fetch_euclid(path: str):
    in_file = open(path, 'r')
    dimension = int(in_file.readline().split(' ')[1])

    result = {}

    fmt = in_file.readline().split(' ')[1]
    print(dimension, fmt)

    in_file.readline()

    for line in in_file.readlines():
        if line == 'EOF':
            break
        words = line.split(' ')
        result[int(words[0]) - 1] = float(words[1]), float(words[2])

    return result, dimension