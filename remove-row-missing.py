import pandas as pd
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    threshold = 0.0
    
    # read argv from command line
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
    # end of read argv

    
    df = pd.read_csv(inputfile)

    #create empty set to store index of row
    missing = set()

    #perform task
    for i in range(len(df)):
        count = 0
        for value in df.iloc[i, :]:
            if value != value:
                count += 1
        if count > threshold*len(df.columns):
            missing.add(i)

    # if no missing, just copy it
    # otherwise shift k row missing
    k = 0
    for i in range(len(df)):
        if i in missing:
            k+=1
        if i + k >= len(df):
            break
        df.iloc[i, :] = df.iloc[i+k, :]

    df.iloc[:(len(df)-k), :].to_csv(outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])