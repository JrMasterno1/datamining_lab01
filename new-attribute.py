import argparse
import pandas as pd

def main():
    # extract argv from command line
    parser = argparse.ArgumentParser(description='Replace missing values with mean/median/mode')
    parser.add_argument('input', type=str)
    parser.add_argument('--newcol', type=str)
    parser.add_argument('--calculation', type=str)
    parser.add_argument('--out', type=str)
    args = parser.parse_args()
    
    print("Example: python new-attribute.py house-prices.csv --newcol sumCol --calculation 'MSSubClass + LotFrontage' --out out.csv")

    inputfile = args.input
    calculation = args.calculation
    outputfile = args.out
    newcol = args.newcol

    print(inputfile)
    print(calculation)
    print(outputfile)
    cal = calculation.split()
    print(cal)
    # read file
    df = pd.read_csv(inputfile)
    result = []
    for i in range(len(df)):
        my_str = ""
        for j in range(0,len(cal)):
            if j % 2 == 0:

                my_str += str(df[cal[j]][i])
            else:
                my_str += cal[j]
        if "nan" in my_str:
            result.append(float("nan"))
        else:
            result.append(eval(my_str))
    df[newcol] = result

    # export data to csv file    
    df.to_csv(outputfile, index=False)

if __name__ == "__main__":
    print("Example: python new-attribute.py house-prices.csv --newcol sumCol --calculation 'MSSubClass + LotFrontage' --out out.csv")
    main()