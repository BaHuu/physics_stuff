import pandas as pd
import matplotlib.pyplot as plt

# Állandók
R = 8.3145 # J/(mol*K) | Gázállandó
n = 1.0 # mol | Anyagmennyiség
T = 420.0 # K | Hőmérséklet
P = 101325.0 # Pa | Nyomás, 1 atm
V = n * R * T / P # m^3 | Térfogat

# Izobár folyamat (állandó nyomás)
def plot_isobaric(ax):
    # A térfogatot 0.1 és 10 között egyenletesen változtatjuk
    V_values = []
    for v in range(1, 101):
        V_values.append(v / 10)

    # A hőmérséklet kiszámolása a térfogat függvényében
    T_values = []
    for v in V_values:
        T_values.append(P * v / (n * R))

    # Értékek megjeleítése, és  pici formázás
    df = pd.DataFrame({'Térfogat (m^3)': V_values, 'Hőmérséklet (K)': T_values})
    df.plot(x='Térfogat (m^3)', y='Hőmérséklet (K)', label='izobár', ax=ax)
    ax.set_ylabel('Hőmérséklet (K)')
    ax.yaxis.set_label_position('right')
    ax.xaxis.set_label_position('top')

# Izoterm folyamat (állandó hőmérséklet)
def plot_isothermal(ax):
    V_values = []
    for v in range(1,101):
        V_values.append(v / 10)

    P_values = []
    for v in V_values:
        P_values.append(n * R * T / v)

    df = pd.DataFrame({'Térfogat (m^3)': V_values, 'Nyomás (Pa)': P_values})
    df.plot(x='Térfogat (m^3)', y='Nyomás (Pa)', label='izoterm', ax=ax)
    ax.set_ylabel('Nyomás (Pa)')
    ax.yaxis.set_label_position('right')
    ax.xaxis.set_label_position('top')

# Izochor folyamat (állandó térfogat)
def plot_isochoric(ax):
    T_values = [t for t in range(100, 501)]
    for v in range(100, 501):
        T_values.append(v)

    P_values = []
    for T in T_values:
        P_values.append(n * R * T / V)

    df = pd.DataFrame({'Hőmérséklet (K)': T_values, 'Nyomás (Pa)': P_values})
    df.plot(x='Hőmérséklet (K)', y='Nyomás (Pa)', label='izochor ', ax=ax)
    ax.set_ylabel('Nyomás (Pa)')
    ax.yaxis.set_label_position('right')
    ax.xaxis.set_label_position('top')

# Függvények futtatása
fig, axs = plt.subplots(2, 2, figsize=(6, 6))
plot_isobaric(axs[0,0])
plot_isothermal(axs[0,1])
plot_isochoric(axs[1,0])
plt.tight_layout()
plt.show()
