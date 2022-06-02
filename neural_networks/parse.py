import numpy as np
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