print("-----------------------------")
print("KFMSCIT028 SURABHI A SALUNKE")
print("-----------------------------")
print(" ")

import pandas as pd
df = pd.read_csv("diabetes.csv")
column_names = df.columns
column_stats = {}
data = df.head()
print(data)

for column_name in column_names:
  column = df[column_name]

  mean = column.mean()
  median = column.median()
  mode = column.mode()
  range = column.max() - column.min()
  variance = column.var()
  standard_deviation = column.std()

  # Add the column stats to the dictionary.
  column_stats[column_name] = {
      "mean": mean,
      "median": median,
      "mode": mode,
      "range": range,
      "variance": variance,
      "standard_deviation": standard_deviation,
      
  }
for column_name, column_stat in column_stats.items():
  print(f"Column name: {column_name}")
  print(f"Mean: {column_stat['mean']}")
  print(f"Median: {column_stat['median']}")
  print(f"Mode: {column_stat['mode']}")
  print(f"Range: {column_stat['range']}")
  print(f"Variance: {column_stat['variance']}")
  print(f"Standard deviation: {column_stat['standard_deviation']}")
  print(" ")
  print("-------------------------------------------------------------")
  print(" ")
