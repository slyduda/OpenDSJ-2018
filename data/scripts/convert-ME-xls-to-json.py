import pandas as pd

#filename
file_name = ["../combined-data-11-6-2018-General-Election-SJC-candidates/combined-ME-460.xls"]

# read the file
excel_file = [pd.ExcelFile(name) for name in file_name]

# turn the excel_file into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excel_file]

# convert to JSON
[df.to_json("../json-11-6-2018-General-Election-SJC-candidates/ME-data.json",orient="table") for df in frames]
