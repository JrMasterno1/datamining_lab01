import sys
import pandas as pd
import numpy as np

def to_string(series):
    my_str = ""
    for col in series:
        my_str += str(col) + " "
    return my_str


def main():
    # check argv from command line
    if (len(sys.argv) != 3):
        print('usage:python remove-row-duplicate.py <inputfile> <outputfile>')
        sys.exit(3)

    # read file
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    df = pd.read_csv(inputfile)

    n = len(df)
    update_df = []
    found = [] # contain duplicate Id
    #remove duplicate
    for i in range(n):
        if to_string(df.iloc[i]) not in found:
            update_df.append(df.iloc[i])
            found.append(to_string(df.iloc[i]))

    #create new dataframe obtained from update_df
    new_df = pd.DataFrame(data=update_df)
    new_df.to_csv(outputfile, index=False)

if __name__ == "__main__":
    main()