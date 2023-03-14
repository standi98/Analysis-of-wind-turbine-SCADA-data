import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as math

#Plot visualising stuff
from cycler import cycler

plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams["axes.labelsize"]= 12
plt.rcParams["figure.facecolor"] = "#f2f2f2"
#plt.rcParams['figure.savefig.dpi'] = 100
plt.rcParams['savefig.edgecolor'] = "#f2f2f2"
plt.rcParams['savefig.facecolor'] ="#f2f2f2"
plt.rcParams["figure.figsize"] = [16,10]
plt.rcParams['savefig.bbox'] = "tight"
plt.rcParams['font.size'] = 14
greens = ['#66c2a4','#41ae76','#238b45','#006d2c','#00441b']
multi =['#66c2a4','#1f78b4','#a6cee3','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f']
plt.rcParams["axes.prop_cycle"] = cycler(color=multi)





def plotTimeline(dataSet: pd.DataFrame, sameGraph = True, plotLegend=False):
    if sameGraph:
        dataSet.plot()

    plt.legend().set_visible(plotLegend)
    plt.show()
        

def plotScatter(dataSet: pd.DataFrame):
    column_names = dataSet.columns

    for col in column_names:
        plt.scatter(range(len(dataSet)), dataSet[col], label=col, s=30, marker= '|')

    plt.show(block = True)


def plotMultipleHistograms(dataSet: pd.DataFrame, bins=None):
    
    #Calculate the size of the histogram
    numCols = len(dataSet.columns)

    neededRows = int(math.ceil(math.sqrt(numCols)))
    neededCols = int(math.ceil(numCols / neededRows))
     
    


    #Calculate Bins if neccesary
    if not bins:
        bins = int(1 + np.log2(len(dataSet)))

    fig, axes = plt.subplots(nrows=neededRows, ncols=neededCols, figsize=(10, 6))
    for i, col in enumerate(dataSet.columns):   
        ax = axes[i // 2, i % 2]
        ax.hist(dataSet[col], bins=bins)
        ax.set_title(col)

    fig.suptitle('Histograms')
    plt.xlabel('Values')
    plt.ylabel('Frequency')

    plt.show(block = True)