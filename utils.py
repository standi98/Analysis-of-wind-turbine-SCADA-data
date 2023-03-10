import pandas as ps


def YNChoice(question: str) -> bool:
    while(True):
        choice = input(question + " [Y/N] ")
        if choice in ["Y", "N"]:
            if choice == "Y":
                return True
            else:
                return False
        
        print("Invalid input! Try again. \n")


def emptyTest(testFile: ps.DataFrame) -> bool:
    return testFile.isnull().sum().isnull().sum()


def interpolateData(file: ps.DataFrame) -> ps.DataFrame:
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


def setNullToZero(file: ps.DataFrame) -> ps.DataFrame:
    return file.fillna(0)

def setZeroToNull(file: ps.DataFrame) -> ps.DataFrame:
    return file.replace(0, ps.NA, method='ffill')


def checkForErrorcode(timeLine: ps.DataFrame, errorCode: int) -> ps.DataFrame:
    timeLine[timeLine != errorCode] = 0
    timeLine = timeLine.replace(errorCode, 1)
    return timeLine
    