print("-----------------------------")
print("KFMSCIT028 SURABHI A SALUNKE")
print("-----------------------------")
print(" ")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('Iris.csv')
hed = data.head()
print(hed)

x = data[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y = data[['Species']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

model = LogisticRegression()
model.fit(x_train,y_train)
pred  = model.predict(x_test)

accuracy = accuracy_score(y_test,pred)
print(accuracy)
