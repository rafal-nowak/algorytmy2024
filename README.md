# Sito Eratostenesa

## Opis projektu

**Sito Eratostenesa** to algorytm służący do znajdowania wszystkich liczb pierwszych mniejszych od liczby **n**. Jest to efektywny sposób eliminowania liczb złożonych poprzez iteracyjne wykreślanie ich wielokrotności.

---

## Zasada działania

1. Tworzymy listę liczb naturalnych od **2** do **n**.
2. Zaczynamy od pierwszej liczby w liście (2) i wykreślamy wszystkie jej wielokrotności (2, 4, 6...).
3. Przechodzimy do następnej liczby, która nie została wykreślona, i eliminujemy jej wielokrotności.
4. Proces powtarzamy, dopóki nie osiągniemy liczby większej niż **pierwiastek z n**.
5. Wszystkie liczby, które pozostały niewykreślone, są liczbami pierwszymi.

---

## Przykład działania

Dla \( n = 10 \):

1. Lista początkowa: **2, 3, 4, 5, 6, 7, 8, 9, 10**  
2. Wykreślamy wielokrotności **2**: **4, 6, 8, 10**  
3. Wykreślamy wielokrotności **3**: **6, 9**
4. Liczby, które pozostały: **2, 3, 5, 7**.

---

## Zastosowanie algorytmu

- **Generowanie listy liczb pierwszych** dla dużych przedziałów.
- **Sprawdzanie, czy liczba jest pierwsza**.
- **Algorytmy kryptograficzne i szyfrowanie** (RSA, generowanie kluczy).

Sito Eratostenesa jest jednym z najefektywniejszych algorytmów do wyznaczania liczb pierwszych w przedziale od **2** do **n** dla umiarkowanie dużych wartości n.

---

## Zalety 

- Złożoność obliczeniowa to **O(n * log log (n))**. Jest to bardzo nietypowa złożoność, ale oznacza ona, że nasz algorytm jest relatywnie szybki.

---

## Wady

- Złożoność pamięciowa to **O(n)**, czyli liniowa – co w przypadku dużych liczb nie jest najlepszym rozwiązaniem.

---

## Ulepszenie Sita Eratostenesa

- Sito Atkina - algorytm opierający się o Sito Eratostenesa, bardziej skomplikowany, ale znacznie szybszy i zajmujący mniej pamięci. Warto go wykorzystać przy większych liczbach.
