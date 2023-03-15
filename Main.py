import os as os
import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
import FileUtils as FU
import plotting
import Analysis

########  File setup #########
#dataFilePath = "ErrorData.csv"
dataFilePath = "job_8DB21580215AF1E_archive_0_file_0.csv"
dataFolderPath = "UnjoinedDataFiles"
checkCode = 6040

### File path fixing
dataFilePath = "Datafiles/" + dataFilePath



########  Main  #############

dataSet = FU.concatenateFilesFromFolder(dataFolderPath)
dataSet = utils.fixNames(dataSet)


dataSet1 = dataSet.iloc[:, [0,2]]
dataSet2 = dataSet.iloc[:, [1,3]]

print(dataSet1)
Analysis.findCosineSimilarity(dataSet1, dataSet2)



#######  Plot the files