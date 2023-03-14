import os
import utils
import pandas as pd


def loadFile(importFile: str):
    importedData = pd.read_csv(importFile, delimiter=";",skiprows=1, index_col="Timestamp", parse_dates=['Timestamp'])
    importedData = utils.setZeroToNull(importedData)
    return importedData


def concatenateFilesFromFolder(fileFolderPath: str) -> pd.DataFrame:
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

    
    #Fix the names of the columns
    totalFrame = totalFrame.rename(columns=lambda x: x.split()[0].replace('-', ''))

    return totalFrame