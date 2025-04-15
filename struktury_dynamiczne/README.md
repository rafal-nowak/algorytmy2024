# Prezentacja o strukturach dynamicznych.

## Wstęp.

Dynamiczne struktury danych to sposób przechowywania danych w pamięci komputera, który pozwala na zmianę ich struktury podczas działania programu.

## 1. Kolejka (FIFO - First In First Out)

FIFO (First In First Out) to metoda, która w programowaniu i magazynowaniu kieruje się zasadą "pierwsze przyszło, pierwsze wyszło".

```python
class Kolejka:
    def __init__(self):
        self.elementy = []

    def enqueue(self, element):
        self.elementy.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.elementy.pop(0)
        raise IndexError("Kolejka jest pusta")

    def peek(self):
        if not self.is_empty():
            return self.elementy[0]
        return None
```
### Operacje na stosie:
- Dodanie elementu na koniec kolejki –> operacja "enqueue"
- Usunięcie elementu z początku kolejki –> operacja "dequeue"
- Podejrzenie pierwszego elementu –> operacja "peek"

Często ten sposób sortowania pojawia się w restauracjach o średnim natężeniu klientów. Dobrym przykładem byłaby kebabiarnia Gorom na kurczakach.
Tam każde zamówienie przyjmują i robią je od razu, gdzie każde następne dostaje następne miejsce na liście zamówień.

---

## 2. LIFO (Last-In, First-Out) 

LIFO to jedna z metod przetwarzania danych. Jest przeciwieństwem FIFO. LIFO działa na zasadzie, że elementy, które weszły jako ostatnie, są usuwane jako pierwsze.

```python
class Stos:
    def __init__(self):
        self.elementy = []

    def push(self, element):
        self.elementy.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elementy.pop()
        raise IndexError("Stos jest pusty")

    def peek(self):
        if not self.is_empty():
            return self.elementy[-1]
        return None

    def is_empty(self):
        return len(self.elementy) == 0

```
### Operacje na stosie:
- Dodanie elementu na szczyt stosu –> operacja "push"
- Usunięcie elementu ze szczytu stosu –> operacja "pop"
- Podejrzenie elementu na szczycie –> operacja "peek"

Ten sposób sortowania jednak nie jest zbytnio efektywny, więc bardzo mało firm go używa. 
Jedyne, które używają LIFO, to firmy wysyłkowe z ogromnymi magazynami.

---

## 3. Lista jednokierunkowa 

### Elementy listy:

- Węzeł (node) -> zawiera dane i wskaźnik na następny węzeł
- Lista zawiera wskaźnik na pierwszy element (głowę)

### Operacje na liście:

- Dodanie elementu na początek/koniec listy

```python
class Wezel:
    def __init__(self, dane):
        self.dane = dane
        self.następny = None

class Lista:
    def __init__(self):
        self.glowa = None

    def dodaj_na_początek(self, dane):
        nowy = Wezel(dane)
        nowy.następny = self.glowa
        self.glowa = nowy

    def dodaj_na_koniec(self, dane):
        nowy = Wezel(dane)
        if not self.glowa:
            self.glowa = nowy
        else:
            biezacy = self.glowa
            while biezacy.następny:
                biezacy = biezacy.następny
            biezacy.następny = nowy

    def wypisz(self):
        biezacy = self.glowa
        while biezacy:
            print(biezacy.dane, end=" -> ")
            biezacy = biezacy.następny
        print("None")
```



---
