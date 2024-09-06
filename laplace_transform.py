from sympy.integrals.transforms import exp, laplace_transform, Heaviside, sinh
from sympy.abc import s, t
from sympy import simplify 

def laplace(h):
    H, cond = laplace_transform(h, t, s)[:2] 
    H = simplify(H)
    print('Laplace Transform:', H) 
    print('Conditions:', cond)

# example of use
h = 104998425.698286*exp(11550000.0*t)*sinh(18857425.5931185*t)*Heaviside(t)
print('h(t): ', h)
laplace(h)


