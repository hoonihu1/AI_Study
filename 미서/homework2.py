from sympy import *

x, y, w0, w1, w2 = symbols("x y w0 w1 w2")

fx = w2*x**2 + w1*x + w0

fprime0 = fx.diff(w0)
fprime1 = fx.diff(w1)
fprime2 = fx.diff(w2)

gx0 = -2*(y-fx)*fprime0
gx1 = -2*(y-fx)*fprime1
gx2 = -2*(y-fx)*fprime2

gx0 = gx0.subs([(x, 0.0), (y,0.0)]) + gx0.subs([(x, 1.0), (y, 1.0)]) + gx0.subs([(x, 1.0), (y, 2.0)]) + gx0.subs([(x, 2.0), (y, 1.0)])
gx1 = gx1.subs([(x, 0.0), (y,0.0)]) + gx1.subs([(x, 1.0), (y, 1.0)]) + gx1.subs([(x, 1.0), (y, 2.0)]) + gx1.subs([(x, 2.0), (y, 1.0)])
gx2 = gx2.subs([(x, 0.0), (y,0.0)]) + gx2.subs([(x, 1.0), (y, 1.0)]) + gx2.subs([(x, 1.0), (y, 2.0)]) + gx2.subs([(x, 2.0), (y, 1.0)])

w0_, w1_, w2_ = 1, 1, 1

for i in range(100000):
    w0a = w0_ - 0.01*gx0.subs([(w0, w0_), (w1, w1_), (w2, w2_)])
    w1a = w1_ - 0.01*gx1.subs([(w0, w0_), (w1, w1_), (w2, w2_)])
    w2a = w2_ - 0.01*gx2.subs([(w0, w0_), (w1, w1_), (w2, w2_)])
    w0_, w1_, w2_ = w0a, w1a, w2a
    
    if i == 4999 or i == 9999 or i == 99999:
        print(i+1)
        print('w0: ', w0_)
        print('w1: ', w1_)
        print('w2: ', w2_)
        print('')