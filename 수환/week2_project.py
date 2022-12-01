import sympy as sym
x, a, b, c = sym.symbols('x a b c') #변수 선언

def func(data):
    fun = sym.poly(a*x**2 + b*x + c) #함수선언
    tmp = 0
    for i in data:
        x_, y_ = i[0], i[1]
        tmp += (y_ - fun.subs(x, x_))**2
    return tmp

data = ((0.0, 0.0), (1.0, 1.0), (1.0, 2.0), (2.0, 1.0))

fun = func(data)
fun_w2 = sym.diff(fun, a)
fun_w1 = sym.diff(fun, b)
fun_w0 = sym.diff(fun, c)

t = 0
w0, w1, w2 = 1, 1, 1
while t <100000:
    w0_, w1_, w2_ = w0, w1, w2
    w0 = w0 - 0.01 * (fun_w0.subs([(a, w2_), (b, w1_), (c, w0_)]))
    w1 = w1 - 0.01 * (fun_w1.subs([(a, w2_), (b, w1_), (c, w0_)]))
    w2 = w2 - 0.01 * (fun_w2.subs([(a, w2_), (b, w1_), (c, w0_)]))
    t += 1

    if t == 5000:
        print(w2, w1, w0)
    elif t == 10000:
        print(w2, w1, w0)

print(w2, w1, w0)