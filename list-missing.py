import numpy as np
import pandas as pd
import math
import sys, getopt

from pandas.core.dtypes.missing import isnull

def isMissingValue(col):
    return any(isNaN(item) for item in col)

def isNaN(item):
    return item != item # python > 2.5 required

def main(argv):
    if (len(argv) != 1):
        print('usage:python list-missing.py <inputfile>')
        sys.exit(2)
    inputfile = argv[0]
    """
    try:
        opts, args = getopt.getopt(argv,"","")
    except getopt.GetoptError:
        print('list-missing.py <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('list-missing.py <inputfile>') 
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    """
    df = pd.read_csv(inputfile)

    print("Columns having missing values:", end="")
    for column in df:
        if isMissingValue(df[column].to_list()):
            print(column, end=",")

if __name__ == "__main__":
    main(sys.argv[1:])