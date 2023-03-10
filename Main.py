import os as os
import pandas as ps
import matplotlib.pyplot as plt


import utils as utils
import plotting

########  File setup #########
#dataFilePath = "ErrorData.csv"
dataFilePath = "exporteddata_55c0f779-d650-45bf-8583-dd490351b69c.csv"
checkCode = 6040





########  Main  #############


dataSet = utils.loadFile(dataFilePath)
