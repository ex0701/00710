print("-----------------------------")
print("KFMSCIT028 SURABHI A SALUNKE")
print("-----------------------------")
print(" ")

import pandas as pd
import numpy as np
from scipy import stats

#load the dataset
data = pd.read_csv('data.csv')
hed = data.head()
print(hed)

#extract 2 variables
x = data['TCS']
y = data['Wipro']
c = stats.pearsonr(x,y)[0]
print(" ")
if c > 0.7 :
  print("positive correlation")
elif c > 0.4:
  print("moderate correlation")
elif c > 0:
  print("weak correlation")
elif c < 0 and c > -0.4:
  print("negative correlation")
elif c < -0.7:
  print("strong negative correlation")
else:
  print("no correlation")

print(" ")
print("Linea Regression")
model = stats.linregress(x,y)
slope = model.slope
intercept = model.intercept
predy = slope*x + intercept
print(predy)
