from control.matlab import *
import matplotlib.pyplot as plt 

s = tf('s')

H = (s+3)/((s+2)*((s+1)**2+2**2))
print(H)

print('\nsystem zeros:', zero(H))
print('system Poles:', pole(H))

pole_zero_plot(H)
plt.show()