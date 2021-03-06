# importing the dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing



# Reading the data
dataset = pd.read_csv('Chess games stats.csv')



# Collecting the data
X =dataset['Number of Blunders'].values  # independent variable
Y=dataset['White Rating'].values # dependent variable

# Mean X and Y
mean_x= np.mean(X)
mean_y =np.mean(Y)


# Total number of values
n = len(X)

# Using the formula to calculate B1 and B2
numer = 0
denom =0
for i in range(n):
    numer+= (X[i]-mean_x)*(Y[i]-mean_y)
    denom +=(X[i]-mean_x)**2
b1 = numer /denom
b0 = mean_y - (b1 * mean_x)

print("The value of B1 :" + str(b1) +"The value of B0"+ str(b0))


# Plotting values and regression line
max_x = np.max(X)
min_x=np.min(X)

# Calculating Line values
x=np.linspace(min_x,max_x,1000)
y= b0 + b1 * x

# Plotting the line
plt.scatter(x,y,color='#58b970',label ='regression line')

plt.scatter(X,Y,c='#ef5423',label ='Scatter Plot')

plt.xlabel('Number of Blunders')
plt.ylabel('players rating')

plt.legend()
plt.show()

ss_t =0
ss_r = 0
for i in range (n):
    y_pred = b0 + b1 * X[i]
    ss_t+=(Y[i]-mean_y)** 2
    ss_r+=(Y[i]-y_pred)**2
r2 = 1 -(ss_r/ss_t)
print("The R^2 Value is :"+str(r2))
