import pandas as pd

def loadFile(path):
    df=pd.read_excel(path, header=0)
    df = df.fillna('')
    return df

def removeValues(df, column, value):
    df = df[df[column] != value]
    return df

def retrieveValues(df,column,value):
    df = df[df[column] == value]
    return df

def categoryProportion(df,column):
    return print(df[column].value_counts() / len(df))

def categoryCount(df,column):
    return print(df[column].value_counts())

def convertColumnToCategorical(df,column):
    df[column] = df[column].astype('category')
    return df