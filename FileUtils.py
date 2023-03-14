import os
import utils
import pandas as ps


def loadFile(importFile: str):
    importedData = ps.read_csv(importFile, delimiter=";",skiprows=1, index_col="Timestamp", parse_dates=['Timestamp'])
    importedData = utils.setZeroToNull(importedData)
    return importedData


def concatenateFilesFromFolder(fileFolderPath: str) -> ps.DataFrame:
    dataFrameList = []
    
    #Create a list of all the files
    csv_files = [file for file in os.listdir(fileFolderPath)]

    #Create a list of dataframes from all of the files, skipping the first row
    dataFrameList = [ps.read_csv(os.path.join(fileFolderPath, file), delimiter=";", skiprows=1) for file in csv_files]

    #Add the files together
    totalFrame = ps.concat(dataFrameList, ignore_index=True)
    

    #Fix indexing
    totalFrame.iloc[:, 0] = ps.to_datetime(totalFrame.iloc[:, 0])
    totalFrame = totalFrame.set_index(totalFrame.columns[0])

    
    #Fix the names of the columns
    totalFrame = totalFrame.rename(columns=lambda x: x.split()[0].replace('-', ''))

    return totalFrame