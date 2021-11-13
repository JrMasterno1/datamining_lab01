import numpy as np
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

def median(col):
    """
    Median(X, n) = 
    { 
        n is odd  -> X[n / 2]
        n is even -> (X[n / 2 -1 ] + X[n / 2]) / 2
    }
    with:
        - X is dataset
        - n is number of values in dataset
    @param col column
    @return median of non-missing values
    """
    X = [item for item in col if not isNaN(item)] # only contain non-missing values
    n = len(X)
    mid = n // 2

    if n % 2 != 0: # n is odd 
        return X[mid]
    else: # n is even
        return (X[mid - 1] + X[mid]) / 2

def mode(col):
    """
    mode is the most frequently occuring value
    @param col column
    @return the most frequently value
    """
    category = dict()

    for item in col:
        # ignore missing values
        if isNaN(item):
            continue 

        # calculate the frequency of each value
        if item not in category.keys():
            category[item] = 0
        else:
            category[item] += 1

    return max(category, key=category.get) 

def impute(col, method):
    """
    Fill missing values with mean, median ( for numeric ) or mode (for categorical)
    @param col column
    @param method mean, median, or mode
    """

    if method == 'mean':
        replace_value = mean(col)
    elif method == 'median':
        replace_value = median(col)
    elif method == 'mode':
        replace_value = mode(col)

    for index, item in enumerate(col):            
        if (isNaN(item)):
            col[index] = replace_value

def main():
    # extract argv from command line
    # usage: python impute.py <inputfile> --method=<mean/median/mode> --columns <list_of_columns> --out <outputfile>
    # or you can type 'python impute.py -h' for help
    parser = argparse.ArgumentParser(description='Replace missing values with mean/median/mode')
    parser.add_argument('input', type=str)
    parser.add_argument('--method', type=str, choices=['mean','median','mode'])
    parser.add_argument('--columns', nargs='+')
    parser.add_argument('--out', type=str)
    args = parser.parse_args()
    
    inputfile = args.input
    method = args.method
    columns = args.columns
    outputfile = args.out

    # read csv file
    df = pd.read_csv(inputfile)
    

    for name in columns:
        if name in df.head():
            impute(col=df[name], method=method)
        else:
            print("Column ['" , name, "'] is not in the dataset") 
    
    # export data to csv file    
    df.to_csv(outputfile, index=False)


if __name__ == "__main__":
    main() 
