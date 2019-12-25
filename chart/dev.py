import chart.Config as config


def off(plt=None):
    if plt:
        plt.savefig(config.chart_path)
