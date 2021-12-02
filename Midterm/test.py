from numpy.lib import math
import sympy as sp
import math
import numpy as np
from sklearn import metrics
#print('O' if None else 'X')

'''pre = [0.6 , 0.7 , 0.5 ,0.4]
re = [0.5 , 0.3 , 0.8 , 0.7]
for i in range(4):
    F1 = 2 * pre[i]*re[i]/(pre[i]+re[i])
    print(F1)'''

#print([n**n for n in range(1,10)])

text = '''1, 3, 5, 7, 9
          8, 6, 4, 2, 0'''
#text = text.split('\n')
#print(text)
#data = [int(i) for i in text.split(', ')] # Fill inside

'''name = 'Euler number'
number = 2.71828
print(f'The {name} is {number:.2f}.') '''# Fill inside

prof = [
    {'name': 'Kang', 'room': 328},
    {'name': 'Park', 'room': 326},
    {'name': 'Kim',  'room': 331},
    {'name': 'Choi', 'room': 327},
]
prof_sort = sorted(prof)
print(prof_sort)


a= [3,29]

b = [10,18]

de = (a[0]*b[0]+a[1]*b[1]) / (math.sqrt((3**2) + (29**2)) + math.sqrt((10**2) + (18**2)))
print(math.sqrt(850))
print(math.sqrt((10**2) + (18**2)))
print(a[0]*b[0]+a[1]*b[1])

'''y_true = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
y_pred = np.array([1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0])

print(metrics.accuracy_score(y_true, y_pred)) 
print(metrics.balanced_accuracy_score(y_true, y_pred)) 
print(metrics.precision_score(y_true, y_pred)) 
print(metrics.recall_score(y_true, y_pred)) 
print(metrics.f1_score(y_true, y_pred))'''

#print(1/4*(0.6+0.8+0.9+0.7))