import numpy as np
import pandas as pd
import argparse

def countMissingValue(col):
    """
    count number of missing values
    @param col column
    @return the number of missing values
    """
    return len([0 for item in col if isNaN(item)])

def isNaN(item):
    """
    check if an item is NaN (missing value)
    @param item an item
    @return true if that item is NaN
    """
    return item != item # python > 2.5 required

def restricted_float(x):
    """
    Restrict float in range [0, 1]
    @param x arg
    @return arg if the condition is satified; raise error otherwise
    """
    try:
        x = float(x)
        if x < 0.0 or x > 1.0:
            raise argparse.ArgumentTypeError(x, " not in range [0.0, 1.0]")
        return x
    except ValueError:
        raise argparse.ArgumentTypeError(x, " not a floating-point literal")

def main():
    # extract argv from command line
    # usage:python delete-column.py <inputfile> --threshold <[0..1]> --out <outputfile>
    # or you can type 'python normalize.py -h' for help
    parser = argparse.ArgumentParser(description='Replace missing values with mean/median/mode')
    parser.add_argument('input', type=str)
    parser.add_argument('--threshold', type=restricted_float)
    parser.add_argument('--out', type=str)
    args = parser.parse_args()
    
    inputfile = args.input
    threshold = args.threshold
    outputfile = args.out
        
    # read file
    df = pd.read_csv(inputfile)

    # delete column if percentage of missing values in column > threshold
    for column in df:
        if (countMissingValue(df[column]) / len(df[column])) > threshold:
            print("Delete: ", column, "-", countMissingValue(df[column]) / len(df[column]))
            del df[column]

    # export data to csv file    
    df.to_csv(outputfile, index=False)

if __name__ == "__main__":
    main()