import os as os
import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
import FileUtils as FU
import plotting

########  File setup #########
#dataFilePath = "ErrorData.csv"
dataFilePath = "job_8DB21580215AF1E_archive_0_file_0.csv"
dataFolderPath = "UnjoinedDataFiles"
checkCode = 6040

### File path fixing
dataFilePath = "Datafiles/" + dataFilePath



########  Main  #############


dataSet = FU.concatenateFilesFromFolder(dataFolderPath)
#Fix the names of the columns
dataSet = utils.fixNames(dataSet)



#######  Plot the files
print(dataSet.head())
#plotting.plotTimeline(dataSet)
plotting.plotMultipleHistograms(dataSet.iloc[:, :5])



plotting.plotHistogramsAgainstEachother()