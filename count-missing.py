import sys
import pandas as pd


def main():
    # check argv from command line
    if (len(sys.argv) != 2):
        print('usage:python count-missing.py <inputfile>')
        sys.exit(2)

    # read file
    inputfile = sys.argv[1]
    df = pd.read_csv(inputfile)

    #init a set of missing row
    missing_row = set()

    #everytime found a missing row, add index to set
    for col in df:
        for index in range(len(df[col])):
            if df[col][index] != df[col][index]:
                missing_row.add(index)

    #display number of missing row
    print("Number of missing row: ", len(missing_row))

if __name__ == "__main__":
    main()
