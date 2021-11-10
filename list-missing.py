import numpy as np
import pandas as pd
import sys

def isMissingValueColumn(col):
    """
    check if a column having missing value
    @param col column 
    @return true if column having missing value
    """
    return any(isNaN(item) for item in col)

def isNaN(item):
    """
    check if an item is NaN (missing value)
    @param item an item
    @return true if that item is NaN
    """
    return item != item # python > 2.5 required

def main(argv):
    # check argv from command line
    if (len(argv) != 1):
        print('usage:python list-missing.py <inputfile>')
        sys.exit(2)

    # read file
    inputfile = argv[0]
    df = pd.read_csv(inputfile)

    # list all columns having missing value
    print("Columns having missing values:", end="")
    for column in df:
        if isMissingValueColumn(df[column]):
            print(column, end=",")

if __name__ == "__main__":
    main(sys.argv[1:]) # ignore --.py