import sys
import pandas as pd



def main():
    # check argv from command line
    if (len(sys.argv) != 3):
        print('usage:python count-missing.py <inputfile> <outputfile>')
        sys.exit(3)

    # read file
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    df = pd.read_csv(inputfile)


    k = 0
    for i in range(len(df)):

        for j in range(i+1, len(df)):
            if df.iloc[i, :].to_string() == df.iloc[j, :].to_string():
                k+=1
            if k + j >= len(df):
                break
            df.iloc[j, :] = df.iloc[j+k, :]

    df.to_csv(outputfile)

if __name__ == "__main__":
    main()