from control.matlab import *
import numpy as np
from scipy.signal import lti, lsim
import matplotlib.pyplot as plt 

R1 = 10000;    # 10 kohms
R2 = 10000;    # 10 kohms
C = 1*10**(-9) # 1nF
fc = 1/(2*np.pi*R2*C)
print(f'Cutoff frequency: {fc/1e3:.2f} kHz')

numerator = [R2]
denominator = [C*R2*R1, R1]
H = lti(numerator,denominator)
print(H)

t = np.linspace(0, 0.001, 1000)

frequencies = [fc/15, fc*7]
u1 = np.sin(2*np.pi*frequencies[0]*t)
u2 = np.sin(2*np.pi*frequencies[1]*t)

_, y1, _ = lsim(H,u1,t)
_, y2, _ = lsim(H,u2,t)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, u1, label='Entrada (1.06 kHz)')
plt.plot(t, y1, label='Saída (1.06 kHz)')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title('Resposta do Circuito para 1.06 kHz')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, u2, label='Entrada (111.44 kHz)')
plt.plot(t, y2, label='Saída (111.44 kHz)')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.title('Resposta do Circuito para 111.44 kHz')
plt.legend()

plt.tight_layout()
plt.show()