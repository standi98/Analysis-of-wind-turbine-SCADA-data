import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def findCosineSimilarity(dataSet1: pd.DataFrame, dataSet2: pd.DataFrame):
    
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

    print(simDataFrame.head())