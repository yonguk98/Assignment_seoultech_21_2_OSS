import sympy as sp
import matplotlib.pyplot as plt


x,y = sp.symbols('x y') # 대수기호 정의
y = 0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 #식 입력

yd = sp.diff(y,x) # 미분식 정의
print(yd) # 미분식 출력
print(float(yd.subs({x:2}))) # x=2일때 y'(2)

roots = sp.solveset(y,x) # y=0 일때 x값 찾기
print(roots)
r0 = float(roots.args[0]) # 찾은 해 중에 첫번째 값을 실수로 캐스팅
print(r0) 


scale = 10
xs = [x/scale for x in range(-4*scale, 10*scale)] # x를 scale만큰 촘촘하게
ys = [0.1*x**3 - 0.8*x**2 - 1.5*x + 5.4 for x in xs] # initialize y
yt = [-3.5*x + 7 for x in xs] # 접선
plt.plot(xs, ys, 'r-', label='y') # x축값, y축값, red line , 이름 y
plt.plot(xs, yt, 'b--', label='tangent line at x=2') # x축값, y축값, blue 점선 , 이름 tangent line at x=2
plt.xlabel('x') # x축에 나타낼 값
plt.ylabel('y')
plt.grid() # 바탕에 그리드 표시
plt.legend() # 범례표시
plt.show() # 표시 = print

sp.pprint(sp.factor(y)) # unicode를 사용해 식 표현(일반적인 식), factor = 인수분해

y = (x**3-8*x**2-15*x + 54)/10 # coefficient를 유리수로 표현하기위해 식 변형
sp.pprint(sp.factor(y))

