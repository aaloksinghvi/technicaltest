#!/usr/local/opt/python/bin/python3.7

import pandas as pd
import numpy as np
import sys

def getProperties(file_name):
    try:
        df = pd.read_csv(file_name)
        df['pricePerSqft'] = df['price'].divide(df['sq__ft'])
        df = df.replace([np.inf, -np.inf], np.nan).dropna()
        averagePricePerSqft = df['pricePerSqft'].mean()
        print("Average Price / SQ.Foot" + str(averagePricePerSqft))
        df = df[df['pricePerSqft']<averagePricePerSqft]
        print("Creating a report for properties sold for less than the average price / sq.foot to sales-data-filtered.csv")
        df.to_csv('sales-data-filtered.csv')
    except:
        print("Exception in getProperties def block")


if __name__ == "__main__":
    print (" TEST3 : Generate a new CSV file that only includes properties sold for less than the average price / sq.foot.")
    
    file_name = input("Enter filename with full path: ")
    if len(file_name) == 0:
        print("Next time please enter something")
        sys.exit()
    try:
        getProperties(file_name)
    except IOError:
        print ("There was an error reading file")
    sys.exit()
    
