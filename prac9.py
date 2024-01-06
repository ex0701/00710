print("-----------------------------")
print("KFMSCIT028 SURABHI A SALUNKE")
print("-----------------------------")
print(" ")


import numpy as np
import matplotlib.pyplot as plt
from statistics import mean, median,mode

exam_score = [35,28,22,18,20,18,42,36,26,50]
print(exam_score)

m1 = mean(exam_score)
print("mean:",m1)
m2 = median(exam_score)
print("median:",m2)
m3 = mode(exam_score)
print("mode:",m3)

plt.hist(exam_score,bins=10,edgecolor="k",alpha=0.6)
plt.xlabel('exam score')
plt.ylabel('frequency')
plt.title('histogram of exam score')
plt.show()

import pandas as pd

data = pd.DataFrame({"height" :[165,170,175,180,170],"weight" :[60,65,70,75,65]})
print(data)

import matplotlib.pyplot as plt
plt.scatter(data["height"],data["weight"])
plt.xlabel("height")
plt.ylabel("weight")
plt.title("scatter plot of height vs weight")
plt.show()
