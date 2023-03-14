import pandas as ps
import matplotlib.pyplot as plt



def plotTimeline(dataSet: ps.DataFrame, sameGraph = True, plotLegend=False):
    if sameGraph:
        dataSet.plot()

    plt.legend().set_visible(plotLegend)
    plt.show()
        

def plotScatter(dataSet: ps.DataFrame):
    column_names = dataSet.columns

    for col in column_names:
        plt.scatter(range(len(dataSet)), dataSet[col], label=col, s=30, marker= '|')

    plt.show(block = True)




    