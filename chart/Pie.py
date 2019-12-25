import matplotlib.pyplot as plt

from chart.dev import off
from container.Vector import c


def pie(H, labels=c(()), radius=1, main='', col=(), clockwise='None'):
    # 获得H向量的内容 并转为列表 对应数据
    data = list(H.get_data())
    label = list(labels.get_data())
    color = list(col)
    plt.pie(data, colors=color, labels=label, counterclock=clockwise, radius=radius)
    plt.title(main)
    off(plt)
    # plt.show()
