import pandas as pd
from typing import List


def YNChoice(question: str) -> bool:
    """
    Simple yes or no question function
    """
    while(True):
        choice = input(question + " [Y/N] ")
        if choice in ["Y", "N"]:
            if choice == "Y":
                return True
            else:
                return False
        
        print("Invalid input! Try again. \n")


def emptyTest(testFile: pd.DataFrame) -> bool:
    """
    This function checks if there are any empty entries in the dataFrame.
    
    Parameters:
    testFile (pandas.DataFrame): The datframe to check.

    Returns:
    bool: Returns true if there are empty cells and false if not
    """
    return bool(testFile.isnull().sum().isnull().sum())


def interpolateData(file: pd.DataFrame) -> pd.DataFrame:
    """
    This function interpolates the data in the dataFrame.

    Parameters:
    dataSet1 (pandas.DataFrame): The datframe to interpolate.

    Returns:
    pandas.DataFrame: The interpolated dataframe
    """
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
    """
    This function takes a timeline of the error codes in a turbine and replaces all of the other codes with zero, and the one searched for with 1.

    Parameters:
    dataSet (pd.DataFrame): The timeline to search for codes in
    errorCode (int): The code to search for

    Returns:
    pd.DataFrame: The resulting timeline.
    """
    timeLine[timeLine != errorCode] = 0
    timeLine = timeLine.replace(errorCode, 1)
    return timeLine


def fixNames(dataSet: pd.DataFrame) -> pd.DataFrame:
    """
    This function fikses the names of the downloaded columns

    Prameters:
    dataSet (pd.DataFrame): The dataFrame to fix the columns names of

    Returns:
    pd.DataFrame: The fixed dataFrame
    """

    #Split out the correct name
    dataSet = dataSet.rename(columns=lambda x: x.split()[0])

    #Remove the wind park and format name in a more readable way
    dataSet = dataSet.rename(columns=lambda x: ''.join([x.split("-")[1], "-", x.split("-")[2]]))
    return dataSet


def removeTimelines(dataSet : pd.DataFrame, stringsToRemove: List[str]) -> pd.DataFrame:
    """
    This function removes columns from a pandas dataframe that contain any of the specified strings.
    
    Parameters:
    dataSet (pandas.DataFrame): the pandas dataframe
    stringsToRemove (list): a list of strings to remove from the column labels
    
    Returns:
    pandas.DataFrame: a new dataframe with the specified columns removed
    """

    # Create a regular expression to match column labels containing any of the specified strings
    regexPattern = '|'.join(stringsToRemove)
    
    # Use filter method to remove columns
    dataSet = dataSet.filter(regex=f"^(?!.*({regexPattern})).*")
