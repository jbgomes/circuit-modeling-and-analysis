from control.matlab import *
import matplotlib.pyplot as plt 

def time_response_info(H):
    S = stepinfo(H, SettlingTimeThreshold=0.01, RiseTimeLimits=(0.0, 1.0))
    print(S)

#example
s = tf('s')
time_response_info(H = (s+3)/((s+2)*((s+1)**2+2**2)))
