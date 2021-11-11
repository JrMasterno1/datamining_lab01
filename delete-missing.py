import numpy as np
import pandas as pd
import sys, getopt

def countMissingValue(col):
    """
    count number of missing values
    @param col column
    @return the number of missing values
    """
    count = 0
    for item in col:
        if isNaN(item):
            count+=1
    return len([0 for item in col if isNaN(item)])

def isNaN(item):
    """
    check if an item is NaN (missing value)
    @param item an item
    @return true if that item is NaN
    """
    return item != item # python > 2.5 required

def main(argv):
    inputfile = ''
    outputfile = ''
    threshold = 0.0
    
    # check argv from command line
    usage = 'usage:python delete-missing.py <inputfile> --threshold <thresholdvalue: 50% ~ 0.5> --out <outputfile>' 
    if (len(argv) != 5):
        print(usage)
        sys.exit(2)
    inputfile = argv[0]
    
    # get the threshold value
    try:
        opts, args = getopt.getopt(argv[1:],"", ["threshold=", "out="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--threshold":
            try:
                threshold = float(arg) # threshold in [0.0, 1.0]
                if threshold > 1.0:
                    threshold = 1.0
                elif threshold < 0.0:
                    threshold = 0.0
            except ValueError:
                print(usage)
                sys.exit(2)
        elif opt == "--out":
            outputfile = arg
        
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
    main(sys.argv[1:]) # ignore --.py