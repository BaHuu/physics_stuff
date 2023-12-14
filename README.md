# Fizika beadandó

### Telepítés

Írd be: `pip install pandas matplotlib`

### Futtatás

Írd be: `py main.py`

## Explanation

A problémánk a következő: ábrázolni kell az izobár, izoterm és izochor folyamatokat. Az egyetemes gáztörvény segítségével ( $pV = nRT$ )

Ugye elsőnek behívjuk a könyvtárakat amiket használni szeretnénk. Ez a `pandas` és a `matplotlib`.

Elsőnek létre kell hoznunk al grafikonokat, mivel 1 ablakban szeretnénk kiírni mind a 3 folyamatot, ezt az elő sorral csinájuk meg.
Utána meghívom a 3 függvényünket ami hozzá adja a subplot-hoz a kiszámolt folyamatot.

```python
fig, axs = plt.subplots(2, 2, figsize=(6, 6))
plot_isobaric(axs[0,0])
plot_isothermal(axs[0,1])
plot_isochoric(axs[1,0])
plt.tight_layout() # Szoros layout, kevesebb üres tér van a grafikonok között
plt.show() # Megjelenítjük az ablakunkat
```

Egy függvény 2 részből áll, kezdem a másodikkal

```python
df = pd.DataFrame({'Térfogat (m^3)': V_values, 'Nyomás (Pa)': P_values})
df.plot(x='Térfogat (m^3)', y='Nyomás (Pa)', label='izoterm', ax=ax)
ax.set_ylabel('Nyomás (Pa)') # Mégegyszer megadjuk az y tengely értékeit mert csak így jeleníti meg azt is, hiába írtuk bele az előző sorba :(
ax.yaxis.set_label_position('right')
ax.xaxis.set_label_position('top')
```

Ez létrehozza a gráfunkat és hozzáadja subplot-hoz.
Az első sor létrehozza a "keretet", ez a gráf két (vagy több, pl.: ha 3D-s a gráf akkor 3) tengelyének az értékeit definiálja.
A harmadik sortól lefelé meg csak kicsicsázom a gráfot.

Az első fele az a kiszámolás

```python
V_values = []
for v in range(1,101):
    V_values.append(v / 10)

 P_values = []
for V in V_values:
    P_values.append(n * R * T / V)
```

Csak az elsőt magyarázom el, bár nem olyan nehéz. A `V_values` az a térfogat. Ezt csak egyenletesen emeljük (0.1-essével)
A `P_values` pedig a nyomás, ezt meg kiszámoljuk az egyetemes gáztörvény segítségével, őgy hogy végig megyünk a térfogat számain egy for loop-al.