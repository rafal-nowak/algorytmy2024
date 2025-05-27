# Prezentacja-wyszukiwanie najmniejszej i największej wartości

## 1. Wstęp 
Wyszukiwanie wartosci minimalnych i maksymalnych to podstawowa operacja w programowaniu.

Znajdywanie wartosci skrajnych jest istotne w analizie danych, sortowaniu i algorytmach

---

## 2. Funkcja wbudowana 
Python oferuje wygodne funkcje min() i max(), które mogą być bezpośrednio użyte do znalezienia najmniejszej i największej wartości w liście czy sekwencji danych. To zdecydowanie ułatwia programistom pisanie kodu.

```python
liczby = [3, 7, 2, 8, 1, 4]
print(min(liczby))
print(max(liczby))
```

---

## 3. Wyszukiwanie ręczne 
Ta technika jest szczególnie użyteczna, gdy uczymy się podstaw programowania lub gdy potrzebujemy lepszego zrozumienia, jak działają algorytmy na poziomie niskopoziomowym. Może być również przydatna w kontekstach, gdzie nie ma dostępu do wbudowanych funkcji, np. w środowiskach ograniczonej funkcjonalności.

Jeśli chcemy samodzielnie zaimplementować takie wyszukiwanie bez korzystania z wbudowanych funkcji, możemy to zrobić poprzez iterację przez wszystkie liczby w pliku. Najpierw ustalamy pierwszą liczbę jako zarówno najmniejszą, jak i największą, a następnie porównujemy każdą kolejną liczbę z tymi wartościami, aktualizując je odpowiednio.

```python
liczby = [3, 7, 2, 8, 1, 4]
najmniejsza = liczby[0]
najwieksza = liczby[0]

for liczba in liczby:
  if liczba < najmniejsza:
    najmniejsza = liczba
  if liczba > najwieksza:
    najwieszka = liczba

print(najmniejsza)
print(najwieksza)
```

---
## 4. Użycie funkcji sorted()

```python
liczby = [3, 7, 2, 8, 1, 4]
sortowanie = sorted(liczby)
print(sortowanie[0])
print(sortowanie[-1])
```


## Przykład nr 1

```python
liczby = [10, 5, 20, 8]
print(min(liczby)) # Wynik: 5
print(max(liczby)) # Wynik: 20
```
---

## Zastosowanie w praktyce
Znajdowanie najlepszego wyniku w grze

Wyszukiwanie najniższej/najwyższej ceny w zbiorze danych

Analiza wyników uczniów


---
