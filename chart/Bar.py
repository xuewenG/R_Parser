import matplotlib.pyplot as plt

from chart.dev import off
from container.Vector import c


def barplot(H, arg=c(()), xlab='', ylab='', main='', col='black', border=''):
    # 获得H向量的内容 并转为列表 对应数据
    data = list(H.get_data())
    # 获得names.arg向量的内容 最终转为range类型 给x刻度进行使用
    x_pos = range(len(list(arg.get_data())))
    # 如果arg没有输入 则默认x上不显示东西
    if x_pos == range(0):
        # 获取刚刚H向量有几个x输入 创建空字符给x刻度
        x_pos = range(len(data))
        temp = []
        for i in x_pos:
            temp.append('')
        plt.xticks(x_pos, temp)
    # arg有输入，获取arg向量的数据并转为list
    else:
        plt.xticks(x_pos, list(arg.get_data()))
    # 设置刻度为0-max 间隔10
    plt.yticks(range(0, max(data), 10))
    # 画图
    plt.bar(x_pos, data, color=col, align='center', alpha=0.8)
    plt.xlabel(xlab)  # x轴上的名字
    plt.ylabel(ylab)  # y轴上的名字
    plt.title(main)  # 标题
    off(plt)
    # plt.show()
