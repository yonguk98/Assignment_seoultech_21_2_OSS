import numpy as np
import matplotlib.pyplot as plt

def buildA(order,xs):
    A = np.empty((0,len(xs)))
    for i in range(order +1 ):
        A = np.vstack((xs**i,A))
    return A.T

true_coeff = [0.1,-0.8,-1.5,5.4]
poly_order = 3
data_range = (-6,12)
data_num = 100 # 데이터 개수
noise_std = 0.5# noise의 범위

x = np.random.uniform(data_range[0],data_range[1],size = data_num)
y = np.matmul(buildA(len(true_coeff)-1 , x),true_coeff)

xn = x + np.random.normal(scale = noise_std,size = x.shape)
yn = y + np.random.normal(scale = noise_std,size = y.shape)

A = buildA(poly_order,xn)
b = yn
coeff = np.matmul(np.linalg.pinv(A),b)

plt.title(f'Curve: y={true_coeff[0]:.3f}*x^3 + {true_coeff[1]:.3f}*$x^2$ + {true_coeff[2]:.3f}*$x$ + {true_coeff[3]:.3f}')
xc = np.linspace(*data_range,100) # 12포함,-6~12를 100개로 나눈 x값 , 순서대로 생성되기 때문에 그래프를 정상적으로 그릴수 있게 하기위함.
plt.plot(xc,np.matmul(buildA(len(true_coeff)-1,xc),true_coeff),'r-')
plt.plot(xn,yn,'b+',alpha=0.5) # alpha는 투명도 , 점으로 표현되기 때문에 xc를 이용한 새로운 노이즈를 만들지 않음.
plt.plot(xc,np.matmul(buildA(poly_order,xc),coeff),'g-')
plt.xlim(data_range)
plt.show()