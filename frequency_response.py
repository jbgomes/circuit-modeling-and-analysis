import matplotlib.pyplot as plt
from control.matlab import *
from math import *
from numpy import *

def bode2(num, den, f0, ff, N):
  H = tf(num, den)

  w = logspace(log10(f0), log10(ff), N, endpoint=True, base=10.0)
  arrayabsHjw, arrayargHjw, omega = frequency_response(H, w)
  #print(arrayabsHjw)
  #arrayabsHjw, arrayargHjw, omega = bode(H)

  plt.figure(figsize=(12, 6))

  plt.subplot(2, 1, 1)
  plt.semilogx(omega,20*log10(arrayabsHjw)) 
  #plt.semilogx(omega,(arrayabsHjw))
  plt.grid(True)
  plt.ylabel('Magnitude |H(jw)|, (dB)')
  plt.xlabel('Frequency, w (rad/s)')
  
  for decade in range(int(log10(f0)), int(log10(ff))+1):
      for i in range(1, 10):
        freq = i * 10**decade
        plt.axvline(x=freq, color='grey', linestyle='--', linewidth=0.5)

  plt.subplot(2, 1, 2)
  plt.semilogx(omega,(180.0/pi)*arrayargHjw) 
  plt.grid(True)
  plt.ylabel('Phase |H(jw)|, (˚)')
  plt.xlabel('Frequency, w (rad/s)') 

  for decade in range(int(log10(f0)), int(log10(ff))+1):
      for i in range(1, 10):
        freq = i * 10**decade
        plt.axvline(x=freq, color='grey', linestyle='--', linewidth=0.5)

  plt.show()

#s = tf('s')
#H = (s+1)/(s**2 + 0.5*s + 1)
#print(H)
#bode2(H, 1e-4, 1e4, 271)