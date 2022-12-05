from sympy import *

data=[(0.0,0.0),(1.0,1.0),(1.0,2.0),(2.0,1.0)]

w2=Symbol('w2')
w1=Symbol('w1')
w0=Symbol('w0')

#사용모델(f) 설정
def f(x):
    f=w2*x**2+w1*x+w0
    return f

#error함수
def Error():
    e=0
    for data_index in range(len(data)):
        e+=expand((data[data_index][1]-f(data[data_index][0]))**2)
    return simplify(e)

#편미분 
dfdw0=diff(Error(),w0)
dfdw1=diff(Error(),w1)
dfdw2=diff(Error(),w2)


n=0.01
before_w0=1
before_w1=1
before_w2=1

#5000번
for i in range(5000):
    after_w0=before_w0-n*(dfdw0.subs({w0:before_w0,w1:before_w1,w2:before_w2}))
    after_w1=before_w1-n*(dfdw1.subs({w0:before_w0,w1:before_w1,w2:before_w2}))
    after_w2=before_w2-n*(dfdw2.subs({w0:before_w0,w1:before_w1,w2:before_w2}))

    before_w0=after_w0
    before_w1=after_w1
    before_w2=after_w2

print("5000번")
print("w0:",after_w0)
print("w1:",after_w1)
print("w2:",after_w2)


#10000번
before_w0=1
before_w1=1
before_w2=1
for i in range(10000):
    after_w0=before_w0-n*(dfdw0.subs({w0:before_w0,w1:before_w1,w2:before_w2}))
    after_w1=before_w1-n*(dfdw1.subs({w0:before_w0,w1:before_w1,w2:before_w2}))
    after_w2=before_w2-n*(dfdw2.subs({w0:before_w0,w1:before_w1,w2:before_w2}))

    before_w0=after_w0
    before_w1=after_w1
    before_w2=after_w2

print("10000번")
print("w0:",after_w0)
print("w1:",after_w1)
print("w2:",after_w2)

#100000번
before_w0=1
before_w1=1
before_w2=1
for i in range(100000):
    after_w0=before_w0-n*(dfdw0.subs({w0:before_w0,w1:before_w1,w2:before_w2}))
    after_w1=before_w1-n*(dfdw1.subs({w0:before_w0,w1:before_w1,w2:before_w2}))
    after_w2=before_w2-n*(dfdw2.subs({w0:before_w0,w1:before_w1,w2:before_w2}))

    before_w0=after_w0
    before_w1=after_w1
    before_w2=after_w2

print("100000번")
print("w0:",after_w0)
print("w1:",after_w1)
print("w2:",after_w2)