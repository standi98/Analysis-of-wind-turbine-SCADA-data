import os as os
import pandas as ps
import matplotlib.pyplot as plt
import utils as utils
import FileUtils as FU
import plotting

########  File setup #########
#dataFilePath = "ErrorData.csv"
dataFilePath = "job_8DB21580215AF1E_archive_0_file_0.csv"
dataFolderPath = "UnjoinedDataFiles"
checkCode = 6040




dataFilePath = "Datafiles/" + dataFilePath
########  Main  #############


dataSet = FU.concatenateFilesFromFolder(dataFolderPath)
#dataSet = FU.loadFile(dataFilePath)
print(dataSet.head())
plotting.plotTimeline(dataSet)
