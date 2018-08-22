#Q.1 - Download the weather dataset 
'''
a.) Plot atleast 20 visualization for the same dataset with different data points.
Ensure that the type of visualization is appropriate and follows this chart.
'''
#importing the required libraries
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
import numpy as np
%matplotlib inline
#importing the data set
df = pd.read_csv("weather.csv")
print("data frame is-")
df
plt.plot([df["Pressure9am"],df["MaxTemp"]]) # plot 1
plt.ylabel("MaxTemp")
plt.xlabel("Pressure9am")
plt.plot(df["Pressure9am"],df["MaxTemp"],'r^') # plot 2
plt.ylabel("MaxTemp")
plt.xlabel("Pressure9am")
plt.hist(df["MinTemp"]) # plot 3
sn.distplot(df["MinTemp"],kde=True) # plot 4
sn.distplot(df["MinTemp"],kde=False) # plot 5
plt.scatter(df["Pressure9am"],df["MaxTemp"],c="g") # plot 6
plt.ylabel("MaxTemp")
plt.xlabel("Pressure9am")
sn.jointplot(df["MinTemp"],df["MaxTemp"],color="r") # plot 7
sn.distplot(df["MinTemp"],hist=False,kde=True,rug=True) # plot 8
sn.kdeplot(df["MinTemp"],shade=True, color="r") # plot 9
plt.figure(figsize=(10,8)) # plot 10
sn.kdeplot(df["MinTemp"],df["MaxTemp"])
plt.figure(figsize=(10,8))  # plot 11
sn.kdeplot(df["MinTemp"],df["MaxTemp"],shade=True)
sn.jointplot(df["MinTemp"],df["MaxTemp"],kind="hex", color="r") #hexbin plot
# plot 12
sn.jointplot(df["MinTemp"],df["MaxTemp"],kind="kde", color="r")  # plot 13
sn.lmplot(x="MinTemp",y="MaxTemp",data=df,hue="Rainfall")  # plot 14
sn.boxplot(x="MinTemp",y="Rainfall",data=df)  # plot 15
plt.figure(figsize=(10,8))  # plot 16
sn.stripplot(x="MinTemp",y="Rainfall",data=df)
sn.countplot(x="MinTemp",data=df)  # plot 17
plt.figure(figsize=(10,8))  # plot 18
sn.swarmplot(x="MinTemp",y="Rainfall",data=df)
plt.figure(figsize=(10,8))  # plot 19
corr=df.corr()
sn.heatmap(corr)
tips=sn.load_dataset("tips")
tips.head()
sn.pairplot(tips)  # plot 20
