from sympy.integrals.transforms import inverse_laplace_transform
from sympy.abc import s, t
from sympy import simplify

def i_laplace(num, den):
    #t,s = symbols("t s")
    #a = Symbol('a', positive = True)
    acm = 0
    i = len(num) - 1

    for k in num:
        acm = acm + s**(i)*k
        i = i - 1
    NUM = simplify(acm)
    print('Numerator:', NUM)

    acm = 0
    i = len(den) - 1

    for k in den:
        acm = acm + s**(i)*k
        i = i - 1 
    DEN = simplify(acm)
    print('Denominator:', DEN)

    H = simplify(NUM/DEN)
    print('H(s):', H)

    h = simplify(inverse_laplace_transform(H, s, t))
    print('Inverse Laplace:', h)

# Example of use
#i_laplace([0, 0, 1], [1, 2, 1])