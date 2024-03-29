import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as math

#Plot visualising stuff
from cycler import cycler
if True:
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
    """
    This function plots timelines from a pandas dataframe.
    
    Parameters:
    dataSet (pandas.DataFrame): the pandas dataframe to plot
    sameGraph (bool): Selects if the timelines should be plotted seperatly or in the same window
    plotLegend (bool): Selects if the legend should be shown, not recomended for large amounts of timelines
    """

    if sameGraph:
        dataSet.plot()

    plt.legend().set_visible(plotLegend)
    plt.show()
        

def plotScatter(dataSet: pd.DataFrame):
    """
    This function plots a scatter plot of all columns in the dataset

    Parameters:
    dataSet (pandas.DataFrame): The datframe to plot. 
    """
    column_names = dataSet.columns

    for col in column_names:
        plt.scatter(range(len(dataSet)), dataSet[col], label=col, s=30, marker= '|')

    plt.show(block = True)


def plotMultipleHistograms(dataSet: pd.DataFrame, bins=None):
    """
    This function plots multiple histograms in different windows. 
    It takes a dataframe and plots one histogram for each of the columns in the dataframe,
    with the individual values in each column separated in predetermined or calculated bins

    Parameters:
    dataSet (pandas.DataFrame): The datframe to plot.
    """
    
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
    plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.85,
                    wspace=0.4,
                    hspace=0.6)

    plt.show(block = True)


def plotHistogramsAgainstEachother(dataSet1: pd.DataFrame, dataSet2: pd.DataFrame):
    """
    This function takes two corresponding dataframes and plots each column next to eachither using plotMultipleHistogram()

    Parameters:
    dataSet1 (pandas.DataFrame): The first datframe to plot.
    dataSet2 (pandas.DataFrame): The second datframe to plot.
    """
    
    #Condatenate the dataSets
    concatenatedDataSet = pd.concat(dataSet1, dataSet2, axis=1)
    interchangedDataSet = concatenatedDataSet.iloc[:, ::2]
    plotMultipleHistograms(interchangedDataSet)
