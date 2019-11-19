import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for file in data_files:
    key_name = file.replace(".csv", "")
    data[key_name] = pd.read_csv("schools/" + file)
