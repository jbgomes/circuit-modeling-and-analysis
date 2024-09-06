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

#example
s = tf('s')
pole_zero(H = (s+3)/((s+2)*((s+1)**2+2**2)))
