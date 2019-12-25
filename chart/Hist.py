import matplotlib.pyplot as plt
from container.Vector import c
from chart.dev import off
import math


# hist(v,main,xlab,xlim,ylim,breaks,col,border)
# v是包含直方图中使用的数值的向量。
# main表示图表的标题。
# col用于设置条的颜色。
# border用于设置每个条的边框颜色。
# xlab用于给出x轴的描述。
# xlim用于指定x轴上的值的范围。
# ylim用于指定y轴上的值的范围。
# break用于提及每个条的宽度。
def hist(H, xlab='', ylab='', xlim=c(()), ylim=c(()), main='', col='black', breaks=5, border=''):
    # 获得H向量的内容 并转为列表 对应数据
    data = list(H.get_data())
    data.sort()
    max_ = math.ceil(max(data) / breaks) * breaks
    plt.hist(data, range(0, max_, breaks), color=col, rwidth=0.98)
    x_data = xlim.get_data()
    y_data = ylim.get_data()
    if len(x_data) != 0:
        plt.xlim(x_data)
    if len(y_data) != 0:
        plt.ylim(y_data)
    plt.xlabel(xlab)  # x轴上的名字
    plt.ylabel('Frequency')  # y轴上的名字
    if main == '':
        main = 'Histogram of H'
    plt.title(main)  # 标题

    off(plt)
    plt.show()
