# Sito Eratostenesa

## 1. Co to jest?
**Polega na wyznaczaniu liczby pierwszych z przedziału ⟨2, n⟩ n∈ℕ.**

Jest to znacznie lepszy sposób niż sprawdzanie pierwszości liczby
dla każdej kolejnej wartości z przedziału.

### Zalety:
- **Złożoność obliczeniowa** to `O(n*log log(n))`. To oznacza, że algorytm jest relatywnie szybki.

### Wady:
- **Złożoność pamięciowa** to `O(n)` - złożoność liniowa. Algorytm zajmuje dużo pamięci i przy większych liczbach będzie to problematyczne. W takim przypadku warto posłużyć się innymi algorytmami. 

## 2. Działanie Sita

1. Stwórz listę dla indeksów z przedziału ⟨0, n⟩. Wszystkie wartości mają być `True`.
2. Ustaw `pierwsze[0] = False` i `pierwsze[1] = False`.
3. Wybierz najmniejszą liczbę z przedziału ⟨2, n⟩. Jest to `2`, która jest liczbą pierwszą.
4. Dla większych wielokrotności liczby `2` ustaw wartość `False`. Przykład: `pierwsze[4] = False`.
5. Wybierz kolejną liczbę `x` z przedziału ⟨2, n⟩. Jeśli `pierwsze[x] = True`, to znaczy, że `x` jest liczbą pierwszą. Wtedy ustaw wartość `False` dla większych wielokrotności `x`.
6. Powtarzaj krok 5 dla `x∈⟨2, √n⟩`.
7. Wszystkie indeksy, których wartość wynosi `True`, są liczbami pierwszymi.

**Pamiętaj!**
- Usuwając wielokrotności liczby pierwszej, zacznij od jej kwadratu! Nie ma sensu usuwać mniejszych wielokrotności, gdyż zostały już usunięte. Pomoże to w optymalizacji algorytmu.

## 3. Implementacja Sita w programowaniu

### Python

**Pamiętaj o `import math`**

#### Sprawdź, czy n>2 ∧ n∈ℤ
```python
def is_range_correct(n):
    if n > 2 and n%1==0:
        return True
    else:
        return False
```
lub
```python
def is_range_correct(n):
    return True if n > 2 and n%1==0 else False
```

#### Sito Eratostenesa
```python
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)  # Tworzymy liste z wszystkimi wartościami True

    # 0 i 1 nie sa liczbami pierwszymi
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return is_prime
```

#### Tworzenie listy z liczbami pierwszymi
```python
def find_prime_numbers(n):
    is_prime = sieve_of_eratosthenes(n)

    # Tworzymy liste z samymi liczbami pierwszymi z podanego przedzialu
    prime_numbers = []

    for x in range(2, n + 1):
        if is_prime[x] == True:
            prime_numbers.append(x)

    return prime_numbers
```

#### Wypisywanie liczb pierwszych
```python
def print_prime_numbers(n):
    is_prime = sieve_of_eratosthenes(n)

    for x in range(2, n+1):
        if is_prime[x] == True:
            print(x)
```

## 4. Zadania

### Znajdź liczby pierwsze z przedziału:
- ⟨2, 60⟩
- ⟨2, 80⟩
- ⟨2, 100⟩
- ⟨2, 653⟩


### Funkcja w Pythonie - rozkład na czynniki pierwsze
Stwórz funkcję w Pythonie, która daną liczbę naturalną rozłoży na czynniki pierwsze.
Rozwiązanie nie musi być oparte na sposobie podanym w prezentacji! Wykorzystaj algorytm Sita Eratostenesa.
Niech funkcja zwróci tablice z czynnikami.

### Rozłóż na czynniki pierwsze:
- 152
- 639
- 1512
- 6537
- 953

## 5. Źródła

- Kanał „Matura Informatyka – Małgorzata Piekarska”
https://www.youtube.com/watch?v=xo2aoAMN-4A
- korepetycjezinformatyki.pl
https://www.korepetycjezinformatyki.pl/sito-eratostenesa/
- algorytm.edu.pl
https://www.algorytm.edu.pl/algorytmy-maturalne/sito-eratostenesa.html
https://www.algorytm.edu.pl/matura-informatyka/zlozonosc-algorytmu
- eduinf.waw.pl
https://eduinf.waw.pl/inf/alg/001_search/0011.php
