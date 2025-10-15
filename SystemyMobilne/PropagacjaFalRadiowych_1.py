import math
import numpy as np
import matplotlib.pyplot as plt

def liczSpadekMocy(f, d, Gt=1.6, Gr=1.6):
    c = 299792458
    lambda_ = c / f
    stosunek = Gt * Gr * (lambda_ / (4 * math.pi * d))**2
    stosunek_dB = 10 * math.log10(stosunek)
    return stosunek_dB

Gt = Gr = 1.6
f1 = 900e6
f2 = 2400e6

d_krotki = np.arange(1, 100.25, 0.25)
d_dlugi = np.arange(1, 10001, 10)

P1_krotki = [liczSpadekMocy(f1, d) for d in d_krotki]
P2_krotki = [liczSpadekMocy(f2, d) for d in d_krotki]
P1_dlugi = [liczSpadekMocy(f1, d) for d in d_dlugi]
P2_dlugi = [liczSpadekMocy(f2, d) for d in d_dlugi]

#f1, krótki zasięg
plt.figure(figsize=(8,5))
plt.plot(d_krotki, P1_krotki)
plt.xlabel("Odległość d [m]")
plt.ylabel("Spadek mocy [dB]")
plt.title("f1 = 900 MHz, zasięg 1–100 m")
plt.grid(True)
plt.show()

#f2, krótki zasięg
plt.figure(figsize=(8,5))
plt.plot(d_krotki, P2_krotki)
plt.xlabel("Odległość d [m]")
plt.ylabel("Spadek mocy [dB]")
plt.title("f2 = 2400 MHz, zasięg 1–100 m")
plt.grid(True)
plt.show()

#f1, długi zasięg
plt.figure(figsize=(8,5))
plt.plot(d_dlugi, P1_dlugi)
plt.xlabel("Odległość d [m]")
plt.ylabel("Spadek mocy [dB]")
plt.title("f1 = 900 MHz, zasięg 1 m – 10 km")
plt.grid(True)
plt.show()

#f2, długi zasięg
plt.figure(figsize=(8,5))
plt.plot(d_dlugi, P2_dlugi)
plt.xlabel("Odległość d [m]")
plt.ylabel("Spadek mocy [dB]")
plt.title("f2 = 2400 MHz, zasięg 1 m – 10 km")
plt.grid(True)
plt.show()
