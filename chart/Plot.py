import matplotlib.pyplot as plt

from chart.dev import off


def plot(H, xlab='', ylab='', main='', col='black', type='o'):
    # 获得H向量的内容 并转为列表 对应数据
    data = list(H.get_data())
    plt.figure()
    x = range(1, len(data) + 1)
    if type == 'p':
        plt.plot(x, data, marker='o', color=col, linestyle="None")
    elif type == 'l':
        plt.plot(x, data, marker='', color=col, linestyle="-")
    elif type == 'o':
        plt.plot(x, data, marker='o', color=col, linestyle="-")
    # 画图
    temp = []
    for i in range(len(data)):
        temp.append(i + 1)
    plt.xticks(temp, range(1, len(data) + 1))
    plt.xlabel(xlab)  # x轴上的名字
    plt.ylabel(ylab)  # y轴上的名字
    plt.title(main)  # 标题
    off(plt)
    # plt.show()
