from control.matlab import *
import matplotlib.pyplot as plt 

s = tf('s')

H = (s+3)/((s+2)*((s+1)**2+2**2))
print(H)

S = stepinfo(H, SettlingTimeThreshold=0.01, RiseTimeLimits=(0.0, 1.0))
print(S)

print('\nsystem zeros:', zero(H))
print('system Poles:', pole(H))

pole_zero_plot(H)
# rlocus(H)
plt.show()