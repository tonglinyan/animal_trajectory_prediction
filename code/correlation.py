import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
from IPython.core.pylabtools import figsize
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas import Series
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot, lag_plot
import seaborn as sns

def ts_plot(data, path):
    figsize(15,9)
    fig = plt.figure()
    gs = gridspec.GridSpec(2,2)

    ax_ts = fig.add_subplot(gs[0, 0:2])
    ax_acf = fig.add_subplot(gs[1, 0])
    ax_pacf = fig.add_subplot(gs[1, 1])
 
    ax_ts.plot(range(len(data)), data)
    plot_acf(data, ax=ax_acf, lags=50)
    plot_pacf(data, ax=ax_pacf, lags=50)
    
    plt.savefig(path)
    plt.show()
    
def correlation(data, path):
    a = data.corr()
    plt.subplots(figsize=(9, 9))
    sns.heatmap(a, annot=True, vmax=1, square=True, cmap="Blues")
    plt.savefig(path)
    plt.show()


def lag_plot(data):
    for i in range (0,400, 50):
        pd.plotting.lag_plot(data, lag = i)
        pyplot.show()


def autocorrelation(data, path): 
    autocorrelation_plot(data)
    plt.savefig(path)
    plt.show()