print("-----------------------------")
print("KFMSCIT028 SURABHI A SALUNKE")
print("-----------------------------")
print(" ")



import numpy as np
import matplotlib.pyplot as plt

# set a random seeed number for reproduce

a= np.random.seed(8)

#generate random sample from a normal distribution

mean = 0
std_dev= 1
num_sample =100
normal_sample = np.random.normal(mean, std_dev, num_sample)

#generate a random sample from a uniform distribution
low = 0
high = 1
uniform_sample = np.random.uniform(low, high, num_sample)

#Create subplots with two columns
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

#Histogram for Normal Distribution
axes[0].hist(normal_sample, bins=20, color="black")
axes[0].set_title("Normal Distribution")

#Histogram for Uniform Distribution
axes[1].hist(uniform_sample, bins = 20, color="black")
axes[1].set_title("Uniform Distribution")

plt.show()
