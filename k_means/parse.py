def parse(path: str):
    """
    提取文本
    :param path:
    :return:
    """
    sentences = []
    emotions = []

    file = open(path)
    file.readline()
    for line in file.readlines():
        line = line[:-1].split(' ')
        emotions.append(int(line[1]) - 1)
        sentence = ''
        for i in range(3, len(line)):
            sentence += line[i] + ' '
        sentences.append(sentence)
    file.close()
    return sentences, emotions