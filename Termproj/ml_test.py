import numpy as np
from sklearn import svm,linear_model
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import csv

data = []
data_name = ['star','review']
target = []
target_names = ['A','B','C']

with open('/Users/yu/Desktop/OSS/Termproj/test2.csv','r') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        data.append([float(i) for i in line[0:2]])
        if line[2] == 'A':
            target.append(0)
        elif line[2] == 'B':
            target.append(1)
        else:
            target.append(2)

data = np.array(data)
target = np.array(target)

model = linear_model.SGDClassifier()
model.fit(data, target)

predict = model.predict(data)
n_correct = sum(predict == target)

cmap = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
clabel = [Line2D([0], [0], marker='o', lw=0, label=target_names[i], color=cmap[i]) for i in range(len(cmap))] 
plt.title(f'svm.SVC ({n_correct}/{len(data)}={n_correct/len(data):.3f})') 
plt.scatter(data[:,0], data[:,1], c=cmap[target], edgecolors=cmap[predict]) 
plt.xlabel(data_name[0])
plt.ylabel(data_name[1])
plt.legend(handles=clabel, framealpha=0.5) 
plt.show()