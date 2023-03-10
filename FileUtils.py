import os
import utils
import pandas as ps


def loadFile(importFile: str):
    importedData = ps.read_csv(importFile, delimiter=";", index_col="TimeStamp", parse_dates=['TimeStamp'])
    importedData = utils.setZeroToNull(importedData)
    return importedData


def concatenateFilesFromFolder(fileFolderPath: str) -> ps.DataFrame:
    dataFrameList = []
    for file in os.listdir(fileFolderPath):
        filePath = os.path.join(fileFolderPath, file)
        df = ps.read_csv(filePath)
        dataFrameList.append(df)
    totalFrame = ps.concat(dataFrameList, ignore_index=True, index_col=0)