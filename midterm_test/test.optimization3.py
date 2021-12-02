# scipy.optimize 의 minimize 함수를 이용해 최솟값, 최댓값을 찾는 예제

from scipy.optimize import minimize
import numpy as np


cost = lambda x: 2.8*x*x + 1.8*x + 0.8 # 그냥 minimize 이용해 최솟값 찾으면 됨

utility = lambda x: 3.2*x*x - 2.9*x - 8.2 
# ㄴ>원래 함수: -3.2*x*x + 2.9*x + 8.2 , 함수에 -1을 곱해서 최솟값을 찾으면 최댓값 나옴

x = np.linspace((-6,12),100)
result = minimize(utility,12)
print(result)