import csv
import pandas as pd

obj = pd.read_csv("./data/data.csv")

#print obj

nparray = obj.values
print (nparray)