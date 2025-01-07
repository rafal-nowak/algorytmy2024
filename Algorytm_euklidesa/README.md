# Algorytm Euklidesa  

## 1. Co to jest?  
Algorytm Euklidesa to jeden z najstarszych znanych algorytmów matematycznych, który służy do wyznaczania największego wspólnego dzielnika (NWD) dwóch liczb naturalnych \( a \) i \( b \). Jest prosty i bardzo wydajny, a jego zastosowanie można spotkać w wielu dziedzinach, takich jak teoria liczb, kryptografia czy informatyka.

---

## 2. Dwie wersje Algorytmu Euklidesa

### a) Niezoptymalizowany Algorytm Euklidesa (odejmowanie):  
- **Zasada działania:** Algorytm działa poprzez iteracyjne odejmowanie mniejszej liczby od większej, aż obie liczby staną się równe. Wynik tej liczby to NWD.  
- **Zalety:** Łatwy do zrozumienia i zaimplementowania.  
- **Wady:** Wydajność spada dla dużych liczb, ponieważ liczba operacji zależy od wartości większej liczby.  

### b) Optymalny Algorytm Euklidesa (modulo):  
- **Zasada działania:** Algorytm wykorzystuje operację modulo (\( a \mod b \)) zamiast odejmowania. Mniejsza liczba zostaje zastąpiona resztą z dzielenia \( a \) przez \( b \), co pozwala szybciej osiągnąć wynik.  
- **Zalety:** Dużo szybszy dzięki logarytmicznej złożoności czasowej.  
- **Wady:** Wymaga zrozumienia operacji modulo, co może być mniej intuicyjne dla początkujących.  

---

## 3. Działanie algorytmu na przykładach  

### Przykład: Wyznacz NWD(48, 18):  

#### Niezoptymalizowany algorytm (odejmowanie):  
1. \( a = 48, b = 18 \): \( a > b \), więc \( a = a - b = 48 - 18 = 30 \).  
2. \( a = 30, b = 18 \): \( a > b \), więc \( a = a - b = 30 - 18 = 12 \).  
3. \( a = 12, b = 18 \): \( b > a \), więc \( b = b - a = 18 - 12 = 6 \).  
4. \( a = 12, b = 6 \): \( a > b \), więc \( a = a - b = 12 - 6 = 6 \).  
5. \( a = 6, b = 6 \): \( a = b = 6 \).
6. Wynik: \( NWD(48, 18) = 6 \).  

#### Optymalny algorytm (modulo):  
1. \( a = 48, b = 18 \): \( a mod b  = 48 mod 18 = 12 ), więc \( a = 18, b = 12 \).  
2. \( a = 18, b = 12 \): \( a mod b  = 18 mod 12 = 6 ), więc \( a = 12, b = 6 \).  
3. \( a = 12, b = 6 \): \( a mod b  = 12 mod 6 = 0 ), więc \( NWD = b = 6 \).  

Oba algorytmy dają ten sam wynik \( NWD(48, 18) = 6 \), ale wersja optymalna wymaga mniej operacji.  

---
## 3.1. Obliczanie NWW (Najmniejsza Wspólna Wielokrotność)

Najmniejsza Wspólna Wielokrotność (NWW) dwóch liczb naturalnych `a` i `b` to najmniejsza liczba, która jest wielokrotnością zarówno `a`, jak i `b`.

### Zależność między NWW i NWD:

NWW(a, b) = (a * b) / NWD(a, b)

### Przykład: Wyznacz NWW(48, 18):

1. Najpierw wyznacz NWD(48, 18) = 6 (np. za pomocą Algorytmu Euklidesa).
2. Następnie oblicz NWW:
   NWW(48, 18) = (48 * 18) / 6 = 144
3. Wynik: NWW(48, 18) = 144

---
# Wyjaśnienie poprawności Algorytmu Euklidesa

## Cel
Chcemy pokazać, dlaczego `NWD(a, b) = NWD(b, a % b)`. Innymi słowy, dlaczego zamiana `a` na resztę z dzielenia `a % b` wciąż prowadzi do poprawnego wyniku.

## Intuicyjne wyjaśnienie
Jeśli `d` jest największym wspólnym dzielnikiem `a` i `b`, to `d` dzieli zarówno `a`, jak i `b`.  
Reszta `r = a % b` jest różnicą `a` i wielokrotności `b`, co oznacza, że `d` musi także dzielić `r`.  
Dlatego `NWD(a, b) = NWD(b, r)`.

## Przykład na liczbach
Weźmy `a = 48` i `b = 18`.

### Krok 1: Znajdź resztę `r = a % b`
r = 48 % 18 = 48 - 2 * 18 = 12
Reszta to `12`.

Pokażmy, że dzielniki wspólne `48` i `18` są takie same jak dla `18` i `12`:

- Dzielniki `48`: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48  
- Dzielniki `18`: 1, 2, 3, 6, 9, 18  
- Wspólne dzielniki `48` i `18`: 1, 2, 3, 6  

Wynik: `NWD(48, 18) = 6`.

### Krok 2: Przejdź do `b = 18` i `r = 12`
Znajdź resztę `r = b % r`:
r = 18 % 12 = 18 - 1 * 12 = 6
Reszta to `6`.

Sprawdźmy dzielniki:
- Dzielniki `18`: 1, 2, 3, 6, 9, 18  
- Dzielniki `12`: 1, 2, 3, 4, 6, 12  
- Wspólne dzielniki `18` i `12`: 1, 2, 3, 6  

Wynik: `NWD(18, 12) = 6`.

### Krok 3: Przejdź do `b = 12` i `r = 6`
Znajdź resztę `r = b % r`:
r = 12 % 6 = 12 - 2 * 6 = 0
Reszta to `0`.

Sprawdźmy dzielniki:
- Dzielniki `12`: 1, 2, 3, 4, 6, 12  
- Dzielniki `6`: 1, 2, 3, 6  
- Wspólne dzielniki `12` i `6`: 1, 2, 3, 6  

Wynik: `NWD(12, 6) = 6`.

### Krok 4: Zakończenie
Gdy `r = 0`, proces kończy się, a wynik to `NWD(6, 0) = 6`.
---
## 5. Implementacja w Pythonie  

### Optymalny algorytm rekurencyjny:  
```python
def nwd_rek(a, b):
    if b == 0:
        return a
    return nwd_rek(b, a % b)
```

### Optymalny algorytm interacyjny:  
```python
def nwd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

---

## 6. Złożoność obliczeniowa  

| Algorytm                    | Złożoność obliczeniowa              
|-----------------------------|---------------------------------|
| **Niezoptymalizowany**      | \( O(max(a, b)) \)            |         
| **Optymalny (modulo)**      | \( O(log(min(a, b))) \)      
---

## 7. Zadania do rozwiązania  

1. Oblicz NWD za pomocą obu wersji algorytmu dla liczb:  
   - \( (a, b) = (144, 84) \)  
   - \( (a, b) = (255, 75) \)  
   - \( (a, b) = (1001, 847) \)  
   - \( (a, b) = (3600, 1260) \)  

2.  Stwórz funkcję w Pythonie, która daną obliczy NWW i NWD dla podanej pary liczb.
    Do wykonania zadania wykorzystaj niezoptymalizowany algorytm Euklidesa .

---


