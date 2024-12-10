# Szukanie określonego elementu w zbiorze
## 1. Wyszukiwanie binarne
**Wyszukiwanie binarne** – zwane również „podziałem na pół”, to algorytm, który w bardzo efektywny sposób odnajduje poszukiwany element w posortowanym zbiorze danych. Ta pozornie trywialna idea sprawia, że algorytm ten doskonale sprawdza się w praktyce, szczególnie przy dużych ilościach danych.
   
### **Zalety**:
- Jest szybkie (złożoność obliczeniowa - **O(log n)**)
  
### **Wady**:
- Może być wykorzystane tylko dla posortowanego zbioru danych
---
### Mechanizm działania
1. Dzielimy zbiór danych na dwie części wyznaczając środkowy indeks `mid`
2. Porównujemy środkowy element w indeksie `mid` z szukaną wartością `x`
3. Jeśli szukana wartość zostanie znaleziona w indeksie `mid`, zwracamy ten indeks
4. W przeciwnym wypadku decydujemy, którą część zbioru będziemy dalej rozpatrywać
5. Jeśli szukana wartość `x` jest mniejsza od środkowego elementu, odrzucamy prawą stronę zbioru danych
6. Jeśli szukana wartość `x` jest większa od środkowego elementu, odrzucamy lewą stronę zbioru danych
7. Kontynuujemy proces aż znajdziemy szukaną wartość 

---

### Implementacja wyszukiwania binarnego
```python
def binary_search(arr, left, right, x):

    # Warunek dla zakończenia szukania wartości
    while left <= right:

        # Wyznaczamy środek rozpatrywanego zbioru danych
        mid = (right + left) // 2

        # Sprawdzamy, czy szukana wartość znajduje się w środku
        if arr[mid] == x:
            return mid

        # Jeśli szukana wartość jest większa, ignorujemy lewą stronę
        elif arr[mid] < x:
            left = mid + 1

        # Jeśli szukana wartość jest mniejsza, ignorujemy prawą stronę
        else:
            right = mid - 1

    # Jeśli dojdziemy tutaj, oznacza to, że wartość nie występuje w zbiorze danych
    return -1
```
---

## 2. Szukanie lidera w zbiorze danych
**Lider** - liczba w zbiorze danych większa niż wszystkie liczby po jej prawej stronie

#### Przykład:
Dla zbioru liczb `[16, 17, 4, 3, 5, 2]` liderem są 17, 5 i 2

**Uwaga**: ostatni element zbioru danych jest zawsze liderem

### Proces znajdowania lidera
1. Zaczynając od ostatniego elementu skanujemy wszystkie liczby w zbiorze danych
2. Ostatni element zawsze jest liderem, więc przenosimy go do `output` i przypisujemy zmiennej `max` jego wartość
3. Po napotkaniu kolejnej liczby sprawdzamy, czy jest większa od `max`
   - Jeśli tak, przenosimy ją do `output` i zmieniamy wartość `max` na tę liczbę 
   - W innym wypadku przechodzimy do następnego elementu

### Implementacja
```python
def leaders(arr):
    result = []
    n = len(arr)

    # przypisujemy zmiennej max wartość ostatniego elementu
    max = arr[-1]

    # ostatni element zawsze jest liderem
    result.append(max)

    # iterujemy po liście od prawej do lewej
    for i in range(n - 2, -1, -1):
        # jeśli wartość jest większa od maxa, to jest liderem
        if arr[i] > max:
            # aktualizujemy wartość zmiennej max
            max = arr[i]
            result.append(max)

    result.reverse()

    return result
```
## 3. Szukanie idola w zbiorze danych
**Idol** - element, który występuje w zbiorze więcej niż połowę razy, czyli więcej niż `n/2` razy, gdzie `n` jest liczbą elementów zbioru.

**Uwaga**: Zakładamy, że każdy rozpatrywany zbiór danych ma idola
#### Przykłady: 

Dla zbioru liczb `[3, 2, 3]` idolem jest 3 (pojawia się 2 razy w 3-elementowym zbiorze)

Dla zbioru liczb `[1, 1, 2, 1, 3, 5, 1]` idolem jest 1 (pojawia się 4 razy w 7-elementowym zbiorze)

### Proces znajdowania idola

1. Inicjujemy zmienne `result` i `count`
2. Iterujemy przez zbiór danych:
   - jeśli `count` jest równy zero, przypisujemy zmiennej `result` aktualny element
   - jeśli aktualny element jest równy `result` zwiększamy `count` o jeden
   - w przeciwnym wypadku zmniejszamy `count` o jeden
3. Zwracamy `result`, czyli znalezionego idola
 
### Implementacja
```python
def majority_element(arr):
    result = 0
    count = 0

    for i in arr:
        if count == 0:
            result = i
        count += (1 if i == result else -1)

    return result
```

## 4. Zadania ##
#### 1. Napisz algorytm wyszukiwania binarnego w wersji rekurencyjnej.

#### 2. Rozwiń funkcjonalność algorytmu szukającego idola poprzez wprowadzenie możliwości rozpatrywania zbiorów danych bez idola (np. `[3, 3, 4, 2, 4, 4, 2, 4]` - brak idola)

#### 3. Napisz funkcję, która znajduje pierwiastek kwadratowy z podanej liczby. Jeśli wartość ta nie jest liczbą wymierną, zaokrąglij ją w dół. Skorzystaj z wyszukiwania binarnego.
---

## Źródła:
- https://www.geeksforgeeks.org/binary-search/#what-is-binary-search
- https://stormit.pl/wyszukiwanie-binarne/#wyszukiwanie-binarne-wprowadzenie
- https://www.youtube.com/watch?v=hDn8iOc30Tk&ab_channel=Computerphile
- https://pl.wikipedia.org/wiki/Wyszukiwanie_binarne
- https://www.geeksforgeeks.org/leaders-in-an-array/
- https://takeuforward.org/data-structure/leaders-in-an-array/
- https://www.geeksforgeeks.org/majority-element/
- https://www.youtube.com/watch?v=7pnhv842keE&ab_channel=NeetCode
