import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, cluster)
from matplotlib.colors import ListedColormap
from chatbot_test import getdata


crawl = getdata()
crawl.reader('/Users/yu/Desktop/OSS/Termproj/test.csv') #데이터 불러오기


crawl.data = np.array(crawl.data) # np array로 저장


features = crawl.data[0, :] # 0행은 이름으로 저장
data = np.array(crawl.data[1:, 1:3],dtype='f8')
data[:,:] = data[:,:]*3+15
# Load a dataset partially
#iris = datasets.load_iris()
#data = data[:,0:2]
#iris.feature_names = iris.feature_names[0:2] # Try [:,2:4] 
color = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)])


# Train a model
model = cluster.KMeans(n_clusters= 3)
model.fit(data)


# Visualize training results (decision boundaries)
x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
xy = np.vstack((xx.flatten(), yy.flatten())).T
zz = model.predict(xy)
plt.contourf(xx, yy, zz.reshape(xx.shape), cmap=ListedColormap(color), alpha=0.2)


# Visualize testing results
plt.title(f'cluster.KMeans')
plt.scatter(data[:,0], data[:,1])#, c=color[iris.target]) 
plt.xlabel(features[1])
plt.ylabel(features[2])


# Visualize training results (mean values)


# Try [:,2:4]
for c in range(model.n_clusters):
    plt.scatter(*model.cluster_centers_[c], marker='+', s=200, color='k')
    plt.show()

