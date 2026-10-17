import numpy as np

import matplotlib.pyplot as plt 
 #we then generate values from -10 to 10 with 100 steps btn

x = np.linspace(-10,10,100)
# for y axix, we get the sin(x)
y = np.sin(x)
#we then use the plot funtion to plot
plt.plot(x, y, marker="x")
plt.show()

from sklearn.datasets import load_iris
iris_dataset = load_iris()
 
 
