from glob import glob
import numpy as np
import matplotlib.pyplot as plt
from sklearn import (datasets, svm,linear_model) # Mission #2 and #3) You need to import some modules if necessary
from matplotlib.lines import Line2D # For the custom legend
import csv

def load_wdbc_data(filename):
    class WDBCData:
        data = []
        target = []
        target_names = ['malignant', 'benign']
        feature_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension',
                         'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error',
                         'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']
    wdbc = WDBCData()
    # TODO
    with open(filename,'r')as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            wdbc.data.append([float(i) for i in line[2:]])
            if line[1] == 'M':
                new_target = 0
            else:
                new_target = 1
            wdbc.target.append(new_target)

    wdbc.data = np.array(wdbc.data)
    wdbc.target = np.array(wdbc.target)  
    return wdbc

if __name__ == '__main__':
    # Load a dataset
    #wdbc = datasets.load_breast_cancer()
    wdbc = load_wdbc_data('/Users/yu/Desktop/OSS/week10/ml/data/wdbc.data.csv') # Mission #1) Implement 'load_wdbc_data()'

    # Train a model
    model = linear_model.SGDClassifier(learning_rate='constant',eta0=1e-6)#svm.SVC()                      
    # Mission #2) Try at least two different classifiers
    model.fit(wdbc.data, wdbc.target)
 
    # Test the model
    predict = model.predict(wdbc.data)
    TP,TN=0,0
    for i in range(len(predict)):
        if predict[i] ==0 and wdbc.target[i]==0:
            TP+=1
        elif predict[i] == 1 and wdbc.target[i] ==1:
            TN+=1
    TPP = TP/sum(wdbc.target==0)
    TNN = TN/sum(wdbc.target!=0)
    accuracy = 0.5*(TPP + TNN)  # Mission #3) Calculate balanced accuracy

    # Visualize testing results
    cmap = np.array([(1, 0, 0), (0, 1, 0)])
    clabel = [Line2D([0], [0], marker='.', lw=0, label=wdbc.target_names[i], color=cmap[i]) for i in range(len(cmap))]
    for (x, y) in [(2,3),(19,20),(21,22)]: # Not mandatory, but try [(i, i+1) for i in range(0, 30, 2)]
        plt.title(f'SGDClassifier (0.5*({TPP:.3f}+{TNN:.3f})={accuracy:.3f})')
        plt.scatter(wdbc.data[:,x], wdbc.data[:,y],c=cmap[wdbc.target], edgecolors=cmap[predict],marker='.')
        plt.xlabel(wdbc.feature_names[x])
        plt.ylabel(wdbc.feature_names[y])
        plt.legend(handles=clabel, framealpha=0.5)
        plt.show()
