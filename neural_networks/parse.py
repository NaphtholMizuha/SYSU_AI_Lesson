import numpy as np
import os
def trans(src: np.ndarray):
    result = np.zeros((10, src.size))
    for i in range(10):
        result[i][np.argwhere(src == i)] = 1
    return result.T

def fetch_data(path):
    file = open(path, 'rb')
    bytes_in_file = file.read()

    magic_num = int.from_bytes(bytes_in_file[0:4], "big")
    match magic_num:
        case 2051:
            images = []
            sample = []
            row = int.from_bytes(bytes_in_file[8:12], "big")
            col = int.from_bytes(bytes_in_file[12:16], "big")
            for byte in bytes_in_file[16:]:
                sample.append(byte)
                if len(sample) >= row * col:
                    images.append(sample)
                    sample = []

            return np.array(images)
        case 2049:
            labels = []
            for byte in bytes_in_file[8:]:
                labels.append(byte)
            return trans(np.array(labels))
        case _:
            return 0

def fit_origin_data():
    parsed = [
        'data/train_img',
        'data/train_label',
        'data/test_img',
        'data/test_label',
    ]

    origin = [
        'origin/train-images-idx3-ubyte',
        'origin/train-labels-idx1-ubyte',
        'origin/t10k-images-idx3-ubyte',
        'origin/t10k-labels-idx1-ubyte'
    ]

    for o, p in zip(origin, parsed):
        np.save(p, fetch_data(o))

def fetch_parsed_data():
    if not (os.path.exists('data/train_img.npy') and
            os.path.exists('data/train_label.npy') and
            os.path.exists('data/test_img.npy') and
            os.path.exists('data/test_label.npy')):
        fit_origin_data()

    return [
        np.load('data/train_img.npy'),
        np.load('data/train_label.npy'),
        np.load('data/test_img.npy'),
        np.load('data/test_label.npy')
    ]