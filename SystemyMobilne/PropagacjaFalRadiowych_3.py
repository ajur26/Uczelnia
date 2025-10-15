import numpy as np
import matplotlib.pyplot as plt

# Parametry
Gt = Gr = 1.6
c = 299792458
f1 = 900e6
f2 = 2400e6
h1 = 30
h2 = 3

def moc_friis(f, d, Gt=1.6, Gr=1.6):
    lamb = c / f
    Pr0 = Gt * Gr * (lamb / (4*np.pi))**2
    Pr = Pr0 / d**2
    return 10 * np.log10(Pr)

def moc_dwutorowa(f, d, h1, h2, Gt=1.6, Gr=1.6):
    d1 = np.sqrt((h1 - h2)**2 + d**2)
    d2 = np.sqrt((h1 + h2)**2 + d**2)
    phi1 = -2 * np.pi * f * d1 / c
    phi2 = -2 * np.pi * f * d2 / c
    lamb = c / f
    Pr0 = Gt * Gr * (lamb / (4 * np.pi))**2
    Pr = Pr0 * np.abs(1/d1 * np.exp(1j*phi1) - 1/d2 * np.exp(1j*phi2))**2
    return 10 * np.log10(Pr)

# Odległości
d_krotki = np.arange(1, 100.25, 0.25)
d_dlugi = np.arange(1, 10001, 10)

# Obliczenia dla każdej częstotliwości i zasięgu
# f1 = 900 MHz
friis_900_short = moc_friis(f1, d_krotki)
dwutor_900_short = moc_dwutorowa(f1, d_krotki, h1, h2)
friis_900_long = moc_friis(f1, d_dlugi)
dwutor_900_long = moc_dwutorowa(f1, d_dlugi, h1, h2)

# f2 = 2400 MHz
friis_2400_short = moc_friis(f2, d_krotki)
dwutor_2400_short = moc_dwutorowa(f2, d_krotki, h1, h2)
friis_2400_long = moc_friis(f2, d_dlugi)
dwutor_2400_long = moc_dwutorowa(f2, d_dlugi, h1, h2)


plt.figure(figsize=(12, 10))

plt.subplot(2,2,1)
plt.plot(d_krotki, friis_900_short, label="Friis")
plt.plot(d_krotki, dwutor_900_short, label="Dwutorowość")
plt.xlabel("d [m]")
plt.ylabel("Spadek mocy [dB]")
plt.title("f1 = 900 MHz, 1–100 m")
plt.legend()
plt.grid(True)

plt.subplot(2,2,2)
plt.plot(d_krotki, friis_2400_short, label="Friis")
plt.plot(d_krotki, dwutor_2400_short, label="Dwutorowość")
plt.xlabel("d [m]")
plt.ylabel("Spadek mocy [dB]")
plt.title("f2 = 2400 MHz, 1–100 m")
plt.legend()
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(d_dlugi, friis_900_long, label="Friis")
plt.plot(d_dlugi, dwutor_900_long, label="Dwutorowość")
plt.xlabel("d [m]")
plt.ylabel("Spadek mocy [dB]")
plt.title("f1 = 900 MHz, 1 m – 10 km")
plt.legend()
plt.grid(True)

plt.subplot(2,2,4)
plt.plot(d_dlugi, friis_2400_long, label="Friis")
plt.plot(d_dlugi, dwutor_2400_long, label="Dwutorowość")
plt.xlabel("d [m]")
plt.ylabel("Spadek mocy [dB]")
plt.title("f2 = 2400 MHz, 1 m – 10 km")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
