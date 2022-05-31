import numpy as np

from genetic import position_based_crossover

if __name__ == '__main__':
    arr = np.arange(0, 5)
    weight = np.array([0, 4, 5, 6, 7])
    print(arr[weight.argsort()][::-1])

