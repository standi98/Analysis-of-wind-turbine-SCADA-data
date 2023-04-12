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
checkCode = 6040


Turbine1Folder = "Turbine1"
Turbine2Folder = "Turbine2"

### File path fixing
dataFilePath = "Datafiles/" + dataFilePath



########  Main  #############

removelist = ["ErrorCode"]

# dataSet1 = FU.concatenateFilesFromFolder(Turbine1Folder)
# dataSet1 = utils.setZeroToNull(dataSet1)
# dataSet1.dropna(axis=1, how='all')
# dataSet1 = utils.fixNames(dataSet1)



# dataSet2 = FU.concatenateFilesFromFolder(Turbine2Folder)
# dataSet2 = utils.setZeroToNull(dataSet2)
# dataSet2.dropna(axis=1, how='all')
# dataSet2 = utils.fixNames(dataSet2)


Analysis.plotCoeficientSideBySide()



# print(dataSet1)
# Analysis.findCosineSimilarity(dataSet1, dataSet2)



#######  Plot the files
