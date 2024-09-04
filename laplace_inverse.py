from math import *
from numpy import *
from control.matlab import *
from sympy.integrals.transforms import exp, inverse_laplace_transform, laplace_transform
#from sympy import Symbol, symbols
from sympy.abc import s, t

def i_laplace(num, den):
    #t,s = symbols("t s")
    #a = Symbol('a', positive = True)
    acm = 0
    i = 2

    for k in num:
        acm = acm + s**(i)*k
        i = i - 1
    NUM = acm
    print('numerator:', NUM)

    acm = 0
    i = 2

    for k in den:
        acm = acm + s**(i)*k
        i = i - 1 
    DEN = acm
    print('denominator:', DEN)

    H = NUM/DEN
    print('H:', H)
    h = inverse_laplace_transform(H, s, t)
    print('inverse laplace:', h)

    #G =  laplace_transform(h, t, s, noconds = True) 
    #print('laplace transform:', G) 
    #if H == G:
    #    print('right')
    #else:
    #    print('no right')
    #g = inverse_laplace_transform(G,s,t)
    #print('last:', g)

#a = Symbol('a', positive = True)
#i_laplace([0,0,1],[1, 2 , 1])