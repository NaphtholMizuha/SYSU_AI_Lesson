from sklearn.feature_extraction.text import CountVectorizer
from parse import parse, parse_
import numpy as np

class NBModel:
    def __init__(self, path):
        train, y_train = parse(path)
        vec = CountVectorizer()
        x_train = vec.fit_transform(train)
        self.vocabulary = vec.vocabulary_
        self.emotion_size = np.zeros(6)
        emotion_indices = {i: [] for i in range(6)}
        for i, emotion in enumerate(y_train):
            emotion_indices[emotion].append(i)
            self.emotion_size[emotion] += 1
        temp = []
        for i in range(6):
            x_emotion = x_train.toarray()[emotion_indices[i]]
            y_emotion = x_emotion.sum(axis=0, keepdims=True)
            temp.append(y_emotion)
        self.x_train = np.vstack(temp)
        self.datasize = len(train)

    def predict(self, test):
        res = []
        for line in test:
            res.append(self.predict_unit(line))
        return np.array(res)

    def predict_unit(self, words):
        # 学霸题, 预测标签值
        temp = []
        # 遍历单词语
        for word in words:
            if self.vocabulary.get(word):
                # 获取词频列
                temp.append(self.x_train[:,self.vocabulary[word]])
            else:
                # 没有加个零
                temp.append(np.zeros(6))
        # 矩阵叠起来
        tf = np.vstack(temp)
        # 特征词数量, 特征总频率
        size = np.sum(tf, axis=1, keepdims=True) + np.size(tf, axis=0)
        # 拉氏来平滑, 加一除上去
        p_unit = (tf + 1) / size
        # 结果乘起来
        p = np.prod(p_unit, axis=0, keepdims=True) * self.emotion_size
        # 最大看出来
        return np.argmax(p)
        # 你学会了吗
if __name__ == '__main__':
    train = NBModel('data/train.txt')
    x_test, y_test = parse_('data/test.txt')
    y_test = np.array(y_test)
    predict = train.predict(x_test)
    print(f'Real Label:\n{y_test}')
    print(f'Predict Label:\n{predict}')
    judges = np.equal(y_test, predict)
    print(f'Accuracy: {np.sum(judges) / np.size(judges)}')

