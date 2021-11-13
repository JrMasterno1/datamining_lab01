import numpy as np
import math
import pandas as pd
import argparse


def isNaN(item):
    """
    check if an item is NaN (missing value)
    @param item an item
    @return true if that item is NaN
    """
    return item != item # python > 2.5 required

def mean(col):
    """
    Mean = Sum / Total Numbers
    @param col column
    @return mean of non-missing values
    """
    sum = 0;
    n = 0;
    for item in col:
        if (not isNaN(item)):
            sum += item
            n+=1
    return sum / n

def minmax(col):
    """
    Transform data in range [0, 1]
    @col column
    """
    max_value = max(col)
    min_value = min(col)
    for item in col:
        col[item] = (item - min_value)/ (max_value - min_value)

def zscore(col):
    """
    Normalizing data so that the mean of all of the values is 0 and the standard deviation is 1
    @col column
    """
    mean_value = mean(col)
    standard_deviation = math.sqrt(sum([(item - mean_value)**2 for item in col] / len(col)))
    for item in col:
        col[item] = (item - mean) / standard_deviation
        
def normalize(col, measure):
    """
    Normalize an attribute using z-score/ min-max normalization 
    @param col attribute
    @param measure z-score or min-max
    """
    if measure == 'minmax':
        minmax(col)
    elif measure == 'zscore':
        zscore(col)

def main():
    # extract argv from command line
    # usage: python normalize.py <inputfile> --measure=<zscore/minmax> --columns <list_of_numeric_columns> --out <outputfile>
    # or you can type 'python normalize.py -h' for help
    parser = argparse.ArgumentParser(description='Replace missing values with mean/median/mode')
    parser.add_argument('input', type=str)
    parser.add_argument('--measure', type=str, choices=['zscore','minmax'])
    parser.add_argument('--columns', nargs='+')
    parser.add_argument('--out', type=str)
    args = parser.parse_args()
    
    inputfile = args.input
    measure = args.measure
    columns = args.columns
    outputfile = args.out

    # read csv file
    df = pd.read_csv(inputfile)
    

    for name in columns:
        if name in df.head():
            normalize(col=df[name], measure=measure)
        else:
            print("Column ['" , name, "'] is not in the dataset") 
    
    # export data to csv file    
    df.to_csv(outputfile, index=False)


if __name__ == "__main__":
    main() 
