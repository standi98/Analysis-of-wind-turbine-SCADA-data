import pandas as pd


def YNChoice(question: str) -> bool:
    while(True):
        choice = input(question + " [Y/N] ")
        if choice in ["Y", "N"]:
            if choice == "Y":
                return True
            else:
                return False
        
        print("Invalid input! Try again. \n")


def emptyTest(testFile: pd.DataFrame) -> bool:
    return testFile.isnull().sum().isnull().sum()


def interpolateData(file: pd.DataFrame) -> pd.DataFrame:
    while (not emptyTest(file)):
        errorFrame = file.isnull().sum()
        print("The different timelines contain this many null values:")
        print(errorFrame)
        
        if not YNChoice("Do you want to interpolate the data?"): break

        file.interpolate(limit= 10, limit_direction='both')
        if (emptyTest(file) == emptyTest(errorFrame)):
            if not YNChoice("The interpolation didn't work, do you want to continue?"): break
        
        if emptyTest(file):
            if not YNChoice("There are still empty fields, do you want to try again?"): break
        
    return file


def setNullToZero(file: pd.DataFrame) -> pd.DataFrame:
    return file.fillna(0)

def setZeroToNull(file: pd.DataFrame) -> pd.DataFrame:
    return file.replace(0, pd.NA, method='ffill')


def checkForErrorcode(timeLine: pd.DataFrame, errorCode: int) -> pd.DataFrame:
    timeLine[timeLine != errorCode] = 0
    timeLine = timeLine.replace(errorCode, 1)
    return timeLine
    