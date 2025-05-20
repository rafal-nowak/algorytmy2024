# Ciąg Fibonacciego

Ciąg Fibonacciego zaczyna się od 0 i 1, a kolejne liczby są sumą dwóch poprzednich:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

Każda liczba w tym ciągu jest większa od poprzedniej, a im wyższa liczba, tym bardziej zbliża się do **złotego stosunku** (około 1.618), znanego także jako **phi**.

## Złoty stosunek i spirala

Złoty stosunek, oznaczany symbolem φ (phi), jest liczbą, która pojawia się, gdy stosunek dwóch liczb jest równy stosunkowi ich sumy do większej z nich. W matematyce jest to:

φ = (1 + √5) / 2 ≈ 1.6180339887

Spirala Fibonacciego jest tworzona poprzez rysowanie ćwiartek okręgów o promieniach odpowiadających liczbom Fibonacciego. Każdy nowy ćwiartek okręgu jest wpisany w kwadrat o boku równym kolejnej liczbie w ciągu Fibonacciego.

## Jak wygląda spirala Fibonacciego?

Spirala Fibonacciego jest zakrzywioną linią, która wygląda jak spiralna forma wchodząca w coraz mniejsze łuki. Możemy ją uzyskać, tworząc kwadraty o bokach odpowiadających liczbom w ciągu Fibonacciego, a następnie rysując ćwiartki okręgów w każdym kwadracie.

![Spirala Fibonacciego](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Fibonacci_spiral_34.svg/200px-Fibonacci_spiral_34.svg.png)

## Spirala Fibonacciego w naturze

Spirala Fibonacciego pojawia się w różnych aspektach przyrody. Oto kilka przykładów:

- **Kwiaty**: Liczba płatków w wielu kwiatach, jak stokrotki, często odpowiada liczbom Fibonacciego.
- **Ananasy**: Układ łusek na owocu ananasa również wykazuje wzór spiralny oparty na liczbach Fibonacciego.
- **Muszle**: Wzór spirali jest widoczny w kształcie muszli ślimaka czy kałamarnicy, gdzie promień rośnie zgodnie z ciągiem Fibonacciego.
- **Liście**: Układ liści na łodydze rośliny również często przyjmuje wzór oparty na liczbach Fibonacciego, co zapewnia optymalne nasłonecznienie i efektywność fotosyntezy.

## Spirala Fibonacciego w sztuce i architekturze

Spirala Fibonacciego jest wykorzystywana w sztuce i architekturze, gdzie jest uważana za element przyciągający uwagę i symbolizujący harmonię:

- **Wielka Piramida w Gizie**: W architekturze piramid zauważono obecność zbliżonego do złotego stosunku w proporcjach budowli.
- **Leonardo da Vinci**: W swoich dziełach artysta często stosował proporcje oparte na złotym stosunku, co można zobaczyć w "Człowieku witruwiańskim".
- **Obrazy i rzeźby**: Wiele dzieł sztuki klasycznej i renesansowej posługiwało się tymi proporcjami w celu osiągnięcia harmonii estetycznej.

## Zastosowanie spirali Fibonacciego w nauce

Spirala Fibonacciego oraz liczby Fibonacciego znalazły zastosowanie w różnych dziedzinach nauki:

- **Fizyka**: Wzory spirali mogą być stosowane do modelowania pewnych zjawisk fizycznych, takich jak trajektorie cząsteczek w polach magnetycznych.
- **Ekonomia**: Analitycy wykorzystują ciąg Fibonacciego w analizie rynku akcji, tworząc tzw. poziomy Fibonacciego, które służą do przewidywania poziomów wsparcia i oporu na rynkach finansowych.


## Metody liczenia n-tego elementu ciągu Fibonacciego

Można wyróżnić dwie najpopularniejsze metody służące do liczenia n-tego elementu ciągu, są to iteracyjna oraz rekurencyjna.

### Metoda iteracyjna
Iteracja (łac. iteratio – powtarzanie) – czynność powtarzania tej samej operacji w pętli z góry określoną liczbę razy lub aż do spełnienia określonego warunku.


```python
def fibonacci(n):
    if n <= 0:
        print("N musi być większe od 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a = 0
    b = 1
    for _ in range(2, n):
        temp = a + b
        a = b
        b = temp
    return b
    
if __name__ == "__main__":
    n = int(input("Podaj wartość n: "))
    print(f"{n}-ty element ciągu Fibonacciego to: {fibonacci(n)}")
```

### Metoda rekurencyjna 
Rekurencja (łac. recurrere – przybiec z powrotem) – technika, w której funkcja lub metoda wywołuje samą siebie w celu rozwiązania problemu.
```python
def fibonacci(n):
    if n <= 0:
        print("N musi być większe od 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input("Podaj wartość n: "))
    print(f"{n}-ty element ciągu Fibonacciego to: {fibonacci(n)}")
```
### Metoda rekurencyjna (zapamiętywanie)

```python
from functools import lru_cache

@lru_cache(maxsize=None)      # brak limitu elementów w pamięci podręcznej
def fibonacci(n):
    if n <= 0:
        print("N musi być większe od 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input("Podaj wartość n: "))
    print(f"{n}-ta liczba Fibonacciego to: {fibonacci(n)}")
```
## Porównanie metod

### Złożoność czasowa
Iteracyjna: O(n) - liniowa

Rekurencyjna: O(ϕⁿ) - wykładnicza (wysoce nieoptymalna przy większych liczbach)

Rekurencyjna (zapamiętywanie): O(n) - liniowa

### Złożoność pamięciowa
Iteracyjna: O(1) - stała

Rekurencyjna: O(n) – liniowa

Rekurencyjna (zapamiętywanie): O(n) - liniowa
