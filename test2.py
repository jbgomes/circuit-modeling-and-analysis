from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s, t
from control.matlab import *
 
a = Symbol('a', positive = True)
# Using inverse_laplace_transform() method

k = 10
R1 = 1e5
R2 = k*R1
Cl = 1e-12
Cg = 0.5e-12
gm = 100e-6
r0 = 1e7

s = tf('s')

H = -R2*r0*(gm*R2-1)/((R2**2 + R1*R2 + r0*R2 + R1*r0*gm*R2) + s*(r0*Cl*R2**2 + R1*Cg*R2**2+r0*R1*R2*Cg + r0*R1*R2*Cl) -s**2*(r0*R1*Cg*Cl*R2**2))

gfg = inverse_laplace_transform(H, s, t)
 
print(gfg)