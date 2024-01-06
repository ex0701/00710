#pvalue is known as significant value
print("-----------------------------")
print("KFMSCIT028 SURABHI A SALUNKE")
print("-----------------------------")
print(" ")

from scipy.stats import ttest_1samp
from scipy.stats import stats
import warnings as warnings
warnings.filterwarnings("ignore")
import numpy as np

age = [45,89,23,46,12,69,45,24,34,67]
age1 = [13,15,14, 10, 18, 19, 26,29,16,22]

avg_age=np.mean(age)
avg_age1=np.mean(age1)

print(avg_age)
print(avg_age1)
print("")
print("-----------------------------------")

t_test,p_value=ttest_1samp(age, 30)

print("pvalue",p_value)
print(ttest_1samp(age, 30))
print("ttest",t_test)
if p_value<0.05:
    print("value rejected")
else:
        print("value accepted\n")

print("")
print("-----------------------------------")

#same step for rejecting value t_testi,p_valuel-ttest_1samp(age1,30)
t_test1,p_value1 = ttest_1samp(age1,30)
print("pvalue", p_value1)
print(ttest_1samp(age1,30))
print("ttest",t_test1)

if p_value1<0.05:
    print("value rejected")
else:
        print("value accepted")
        
print("")
print("-----------------------------------")

# perform the ttest value on two data test print("KFMSCIT 24 MANISHA PANIGRAHY")

subA=[20,18,16, 14, 12, 10,8,6,4,2]
subB=[20, 19,17,15,13,11,9,7,5,3]

t_test,p_value=stats.ttest_ind(subA, subB)
alpha=0.05

print(p_value)

if p_value<alpha:
    print("there is a significant differnce in both this subject")
else:
        print("there is a no significant difference in both this subject")
        # if your p value is less than 0.05 you'll reject the hypothesis

print("")
print("-----------------------------------")
