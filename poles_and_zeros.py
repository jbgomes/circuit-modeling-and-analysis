from control.matlab import *
import matplotlib.pyplot as plt 

def pole_zero(H):
    #s = tf('s')
    print(H)

    print('system Poles:', pole(H))
    print('\nsystem zeros:', zero(H))

    pole_zero_plot(H)
    # rlocus(H)
    plt.show()

def time_response_info(H):
    S = stepinfo(H, SettlingTimeThreshold=0.01, RiseTimeLimits=(0.0, 1.0))
    print(S)

#example
s = tf('s')
pole_zero(H = (s+3)/((s+2)*((s+1)**2+2**2)))
