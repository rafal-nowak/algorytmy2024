# Metoda Monte Carlo (obliczanie przybliżonej wartości liczby π, symulacja ruchów Browna) 

## 1. Co to jest?
Metoda Monte Carlo (MC) została opracowana między innymi przez polskiego naukowca Stanisława Ulama oraz węgiersko — amerykańskiego naukowca Johna von Neumanna. Wykorzystano ją podczas prac nad bombą jądrową w celu symulacji procesu rozpadu jąder cząsteczek. Proces był na tyle skomplikowany, że zastosowanie klasycznych modeli obliczeniowych nie zdawało egzaminu.

Metoda polega na przeprowadzeniu procesu w losowy sposób, zakładając, że po wystarczająco dużej liczbie prób otrzymamy wynik zbliżony do rzeczywistego.

### Np:
![POL_województwo_łódzkie_1950](https://github.com/user-attachments/assets/a422d397-c5e3-40e2-a69f-11f41a6b70fd)
Na obrazku przedstawiono obszar Polski z podziałem na województwa. Losowo umieszczono 84 punkty, z czego 6 z nich znajduje się w województwie Łódzkim. Szacując metodą Monte Carlo, możemy stwierdzić, iż województwo Łódzkie stanowi 6/84 (około 7%) powierzchni Polski. Czyli 6 / 84 x 322 575 km² = 23 041 km². Prawdziwa powierzchnia województwa łódzkiego jest jednak równa 18 219 km².
### Zalety:
- Prostota
- Szybkość w otrzymywaniu wyniku
### Wady:
- Różny wynik zalerzny od ilości wylosowanych punktów oraz ich umiejscowienia (za każdym razem wynik bedzie inny)
- Brak dokładnego wyniku

---

## 2. Szacowanie liczby π
- przybliżenie π można obliczyć:
  
  **π = 4 x liczba punktów w okregu / liczba wszystkich punktów** 
- Wideo wyjaśniające, jak metoda Monte Carlo może w łatwy sposób znaleźć liczbę π:
  https://www.youtube.com/watch?v=ELetCV_wX_c
  
### Implementacja w Pythonie
```python
import random
import matplotlib.pyplot as plt

def monte_carlo_pi_with_visualization(num_points):
    inside_circle = 0
    points_inside = []
    points_outside = []

    for _ in range(num_points):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:  # Punkt wewnątrz okręgu
            inside_circle += 1
            points_inside.append((x, y))
        else:
            points_outside.append((x, y))

    # Przybliżenie liczby π
    pi_estimate = 4 * (inside_circle / num_points)

    # Wizualizacja
    plt.figure(figsize=(6, 6))
    plt.scatter(*zip(*points_inside), color="blue", s=1, label="Inside Circle")
    plt.scatter(*zip(*points_outside), color="red", s=1, label="Outside Circle")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Approximation of π\nEstimate: {pi_estimate:.5f} (Points: {num_points})")
    plt.legend()
    plt.show()

    return pi_estimate

# Przykład użycia
num_points = 10_000  # Liczba punktów do wygenerowania
pi_approximation = monte_carlo_pi_with_visualization(num_points)
```

#### Pętla `for _ in range(num_points)` - generuje losowy punkt i przypisuje do koła lub nie:
```python
for _ in range(num_points):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:  # Punkt wewnątrz okręgu
            inside_circle += 1
            points_inside.append((x, y))
        else:
            points_outside.append((x, y))
```

#### Szacowanie wartości π na podstawie wylosowanych punktów:
``` python
 # Przybliżenie liczby π
    pi_estimate = 4 * (inside_circle / num_points)
```
#### Wizualizacja graficzna:
``` python
# Wizualizacja
    plt.figure(figsize=(6, 6))
    plt.scatter(*zip(*points_inside), color="blue", s=1, label="Inside Circle")
    plt.scatter(*zip(*points_outside), color="red", s=1, label="Outside Circle")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Approximation of π\nEstimate: {pi_estimate:.5f} (Points: {num_points})")
    plt.legend()
    plt.show()
```

#### Przykłady:
* dla `num_points` = 100
  
  ![image](https://github.com/user-attachments/assets/c13eacec-7a3b-4640-925b-7bb79f28ba41)

* dla `num_points` = 1000

  ![image](https://github.com/user-attachments/assets/3f97ba14-45d0-4ffb-8af6-e61d1cddcd38)

* dla `num_points` = 10000

  ![image](https://github.com/user-attachments/assets/ce812189-5b66-4923-a69a-647505255611)

---

## 3. Ruchy Browna

### Co to?
**Ruchy Browna** (o których możesz przeczytać m.in. w e‐materiale Modelowanie ruchów Browna) zostały opisane — niezależnie — przez Alberta Einsteina, w  roku oraz przez polskiego fizyka Mariana Smoluchowskiego, w  roku. Ich nazwa pochodzi od botanika Roberta Browna, który pod mikroskopem zaobserwował chaotyczne ruchy pyłku kwiatowego. Ruchy Browna powodowane są nieustannym zderzaniem się cząsteczek płynu w danym ośrodku. Przykładowy model takiego procesu może polegać na umieszczeniu wirtualnej cząsteczki w wirtualnym płynie, w którym — co pewien określony czas — cząsteczka zostaje przemieszczona w losowym kierunku, w wyniku wirtualnej kolizji. Cały proces ma charakter uśredniony. Dzięki temu każda kolizja powoduje przesunięcie cząsteczki o określoną z góry odległość.

Wizualizacja - https://www.youtube.com/shorts/Vm_UlcS4FJE

**Idea** - Ruch Browna jest modelem losowym, który opisuje zmianę pozycji cząsteczki jako sumę drobnych, przypadkowych kroków.

### Implementacja w Pythonie

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_brownian_motion(steps, delta_t=1, scale=1):
    # Początkowe położenie
    x, y = 0, 0
    positions = [(x, y)]
    
    for _ in range(steps):
        # Wygeneruj losowe zmiany pozycji (Gaussowskie)
        dx = np.random.normal(loc=0, scale=scale * np.sqrt(delta_t))
        dy = np.random.normal(loc=0, scale=scale * np.sqrt(delta_t))
        x += dx
        y += dy
        positions.append((x, y))
    
    return positions

# Symulacja i wizualizacja
steps = 500
positions = simulate_brownian_motion(steps)
x_vals, y_vals = zip(*positions)

plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, marker="o", markersize=2, linestyle="-")
plt.title("Symulacja ruchów Browna")
plt.xlabel("x")
plt.ylabel("y")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
```
### Jednak po wykonaniu kilku prób można dojść do wniosku, że powinna istnieć zależność w tego typu ruchach. Stosując metodę MC, możemy sprawdzić, na jakiej podstawie to działa.

#### Program badający ruchy Browna
``` python
import numpy as np
import matplotlib.pyplot as plt

def brownian_x_experiment(trials, steps, delta_t=1, scale=1):
    final_x_positions = []

    for _ in range(trials):
        x = 0
        for _ in range(steps):
            dx = np.random.normal(loc=0, scale=scale * np.sqrt(delta_t))
            x += dx
        # Zapisz końcowe położenie na osi x
        final_x_positions.append(x)

    return final_x_positions

# Parametry eksperymentu
trials = 10_000  # Liczba prób
steps = 100  # Liczba kroków w każdej próbie
final_x_positions = brownian_x_experiment(trials, steps)

# Wizualizacja wyników
plt.figure(figsize=(10, 6))
plt.hist(final_x_positions, bins=30, color="skyblue", edgecolor="black")
plt.title(f"Wynik eksperymentu dla {trials} prób")
plt.xlabel("Końcowe położenie na osi X")
plt.ylabel("Liczba zakończonych prób dla danej pozycji")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```
#### Efekt:
![image](https://github.com/user-attachments/assets/81c80df7-d15b-43c3-8ffb-77f274b4cedf)

Przeprowadzony eksperyment to nic innego jak puszczone kulki na desce Galtona. Kulka
zaczyna swoją wędrówkę od góry, a następnie natrafia na przeszkodę, która powoduje jej
ruch w lewo lub w prawo z jednakowym prawdopodobieństwem.

**Deska Galtona:**

![image](https://github.com/user-attachments/assets/e0554a3b-b8de-4b78-ae80-c1b49f2017ed)

Eksperyment wizualizuje rozkład dwumianowy (w Polsce zwany także rozkładem
Bernoulliego), który w nieskończoności dąży do rozkładu normalnego, znanego jako
rozkład Gaussa.

Wykorzystując pozyskaną wiedzę, przekształcamy początkowy program, aby przypominał on bardziej deskę Galtona (tak, aby wartość poruszała się tylko w górę lub w dół).

**Przykłady**:

1. ![image](https://github.com/user-attachments/assets/754327f8-b66f-4abd-8fe5-836193409288)

2. ![image](https://github.com/user-attachments/assets/df9c0247-abf5-4b94-a50b-3cc283fe85ab)

3. ![image](https://github.com/user-attachments/assets/62385027-fa96-4f02-baa6-003c0130e040)

Czy przedstawione wykresy nie kojarzą się przypadkiem z giełdą?

#### W taki oto sposób, z chaotycznych ruchów pyłków kwiatów w wodzie, udało nam się udowodnić tezę rozkładu naturalnego oraz stworzyć symulator wykresów giełdowych.

---

## 4. Zadania:
- Samodzielnie zbadaj, czy metoda Monte Carlo jest skuteczna w szacowaniu liczby π.
- Zbadaj, czy metoda szacowania Monte Carlo jest szybsza od dokładnych obliczeń matematycznych.
- W jakich przypadkach metoda ta będzie skrajnie niewłaściwa?
- Podaj przykład innych znanych wykresów, które kojarzą się z efektem badania ruchów Browna.

--- 

## 5. Dodatkowy materiał:
- Wikipedia - https://pl.wikipedia.org/wiki/Metoda_Monte_Carlo
- Szacowanie liczby π - https://www.mathematica.pl/?przyblizenie-liczby-pi-metoda-monte-carlo.,191
- Symulacja ruchów Browna - https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi5loGu0vKJAxWQKRAIHTpTMUIQFnoECA0QAQ&url=https%3A%2F%2Fzpe.gov.pl%2Fpdf%2FPOYhAftXy&usg=AOvVaw0qUAwGGaECmmVo2xHqnFf_&opi=89978449
  


