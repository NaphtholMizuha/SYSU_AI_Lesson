import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif']=['Noto Sans SC']   # 用黑体显示中文


def figure(x, y, x_label, y_label, title: str):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    title = title.split(' ')[0]
    plt.savefig(f'{title}.pdf')
    plt.show()