import matplotlib.pyplot as plt
from control.matlab import *
from math import *
from numpy import *

#cm = 1/2.54  # centimeters in inches

def bode2(H, w):
  arrayabsHjw, arrayargHjw, omega = frequency_response(H, w)

  plt.figure(figsize=(12, 6))

  plt.subplot(2, 1, 1)
  plt.semilogx(omega,20*log10(arrayabsHjw)) 
  plt.grid(True)
  plt.ylabel('Magnitude |H(jw)|, (dB)')
  plt.xlabel('Frequency, w (rad/s)') 
  
  plt.subplot(2, 1, 2)
  plt.semilogx(omega,180.0/pi*arrayargHjw) 
  plt.grid(True)
  plt.ylabel('Phase |H(jw)|, (˚)')
  plt.xlabel('Frequency, w (rad/s)') 
  plt.show()

s = tf('s')

H = (s+1)/(s**2 + 0.5*s + 1)
print(H)
inputfreq = logspace(-2, 2, num=3*90+1, endpoint=True, base=10.0)
bode2(H, inputfreq)