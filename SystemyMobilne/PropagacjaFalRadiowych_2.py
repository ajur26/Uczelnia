import numpy as np
import matplotlib.pyplot as plt

c = 299792458 

d_krotki = np.arange(1, 100.25, 0.25)
tau_krotki = d_krotki / c

plt.figure(figsize=(8,5))
plt.plot(d_krotki, tau_krotki*1e9)  
plt.xlabel("Odległość d [m]")
plt.ylabel("Opóźnienie sygnału [ns]")
plt.title("Opóźnienie sygnału w funkcji odległości (1–100 m)")
plt.grid(True)
plt.show()

d_dlugi = np.arange(1, 10001, 10)
tau_dlugi = d_dlugi / c

plt.figure(figsize=(8,5))
plt.plot(d_dlugi, tau_dlugi*1e6)  
plt.xlabel("Odległość d [m]")
plt.ylabel("Opóźnienie sygnału [µs]")
plt.title("Opóźnienie sygnału w funkcji odległości (1 m – 10 km)")
plt.grid(True)
plt.show()
