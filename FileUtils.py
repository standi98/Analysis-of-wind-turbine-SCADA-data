import os
import utils
import pandas as pd


def loadFile(importFile: str) -> pd.DataFrame:
    """
    This function loads a .csv file

    Parameters:
    importFile (str): the file path
    
    Returns:
    pandas.DataFrame: the loaded dataframe
    """
    importedData = pd.read_csv(importFile, delimiter=";",skiprows=1, index_col="Timestamp", parse_dates=['Timestamp'])
    return importedData


def concatenateFilesFromFolder(fileFolderPath: str) -> pd.DataFrame:
    """
    This function concatenates all of the .csv files in a folder.
    They are concatenated in the same order they are listed in, and they are added underneath eachother
    
    Parameters:
    fileFolderPath (str): the folder path
    
    Returns:
    pandas.DataFrame: the concatenaded dataframe
    """


    dataFrameList = []
    
    #Create a list of all the files
    csv_files = [file for file in os.listdir(fileFolderPath)]

    #Create a list of dataframes from all of the files, skipping the first row
    dataFrameList = [pd.read_csv(os.path.join(fileFolderPath, file), delimiter=";", skiprows=1) for file in csv_files]

    #Add the files together
    totalFrame = pd.concat(dataFrameList, ignore_index=True)
    

    #Fix indexing
    totalFrame.iloc[:, 0] = pd.to_datetime(totalFrame.iloc[:, 0])
    totalFrame = totalFrame.set_index(totalFrame.columns[0])

    return totalFrame