import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from typing import List
import mplcursors

def findCosineSimilarity(dataSet1: pd.DataFrame, dataSet2: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes in dataFrames with timelines from two turbines, and returns a dataframe with cosine similarities between the timelines.
    It returns a dataframe with the two first columns as names of the timeseries, and the third column as the similarity of the two.

    Prarameters:
    dataSet1 (pd.DataFrame): The first dataFrame
    dataSet2 (pd.DataFrame): The second dataFrame

    Returns:
    pd.DataFrame: The resulting similarities in a new dataFrame
    """


    #Find column names
    colNames1 = [name for name in dataSet1.columns]
    colNames2 = [name for name in dataSet2.columns]

    simDataFrame = pd.DataFrame(columns=['Turbine 1', 'Turbine 2', 'Similarity'])
    
    for col1, col2 in zip(colNames1, colNames2):
        #Find the similarity for each column in each dataset
        sim = cosine_similarity(dataSet1[col1].values.reshape(1, -1), dataSet2[col2].values.reshape(1, -1))[0][0]

        #Store the similarity in a new dataFrame, where each timeseries has its own row
        simRow = pd.DataFrame({'Turbine 1': col1, 'Turbine 2': col2, 'Similarity': sim}, index=[0])
        simDataFrame = pd.concat([simDataFrame, simRow], ignore_index=True)

    return simDataFrame


def plotCoeficientSideBySide(dataSets: List[pd.DataFrame] = 0):
    """
    This function plots datasets of cosine smilarities next to eachother

    Parameters: 
    dataSes ([pd.DataFrame]): The list of datasets to plot next to eachother
    """

    #Test code
    if dataSets == 0: 
        # create a sample dataframe
        df1 = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'foo'], 'B': ['one', 'one', 'two', 'two'], 'C': ['x', 'y', 'z', 'w'], 'D': [1, 2, 3, 8]})
        df3 = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'foo'], 'B': ['one', 'one', 'two', 'two'], 'C': ['x', 'y', 'z', 'w'], 'D': [5, 6, 3, 8]})
        df2 = pd.DataFrame({'A': ['foo', 'bar', 'baz', 'foo'], 'B': ['one', 'one', 'two', 'two'], 'C': ['x', 'y', 'z', 'w'], 'D': [9, 4, 11, 1]})

        #put the dataframes into a list
        dataSets = [df1, df2, df3]


    #Select the first dataset as a base
    dataSet = dataSets[0]

    #Concatenate the last column of each to the base
    for i in range(1, len(dataSets)):
        dataSet = pd.concat([dataSet, dataSets[i].iloc[:, -1]], axis=1)


    # plot all columns as points next to each other, as well as adding cursors to each
    fig, ax = plt.subplots()
    for i in range(3, len(dataSet.columns)):
        cursor1 = mplcursors.cursor(ax.scatter([i]*len(dataSet), dataSet.iloc[:, i], marker='o', zorder=2), hover=False)
        cursor1.connect("add", lambda sel: sel.annotation.set_text(f"Value: {sel.target[1]}\n Timeseries: {dataSet.iloc[i, 1]}"))


    #draw lines between points that are on the same line in plotted table
    for i in range(len(dataSet)):
        for j in range(4, len(dataSet.columns)):
            ax.plot([[j-1]*len(dataSet), [j]*len(dataSet)], [dataSet.iloc[i, j-1], dataSet.iloc[i, j]], color='gray', linestyle='--', zorder=1)


    plt.show()