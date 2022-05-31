if __name__ == '__main__':
    arr = [1, 1, 4, 5, 1, 4]
    tup = (1, 1, 4, 5, 1, 4)
    tup_ = (1, 1, 4, 5, 1, 4)
    dic = dict()
    dic[arr] = 1
    dic[tup] = 'I am a value.'
    print(dic[tup_])
