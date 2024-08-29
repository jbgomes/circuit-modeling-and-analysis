from control.matlab import *
import matplotlib.pyplot as plt 

s = tf('s')

H = (s+3)/((s+2)*((s+1)**2+2**2))
print(H)

print('dc gain:', dcgain(H))