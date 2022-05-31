from PIL import Image
import numpy as np
if __name__ == '__main__':
    data = []
    for i in range(10):
        img = Image.open('image/' + str(i) + '.png').convert('L')
        arr = np.array(img)
        arr = 255 - arr
        arr[arr < 100] = 0
        arr[0,:] = 0
        arr[-1,:] = 0
        arr[:,0] = 0
        arr[:,-1] = 0
        data.append(arr.flatten() / 255)
    data = np.array(data)
    print(data)
    np.save('data/hand_written.npy', data)