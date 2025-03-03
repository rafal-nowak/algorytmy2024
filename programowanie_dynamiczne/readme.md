# Programowanie Dynamiczne: najdłuższy wspólny podciąg i problem plecakowy

## Czym jest programowanie dynamiczne?
Programowanie dynamiczne (DP) to technika  stosowana do rozwiązywania problemów algorytmicznych poprzez podział na mniejsze podproblemy. Zamiast rozwiązywać je wielokrotnie, ich wyniki są zapisywane i ponownie wykorzystywane w przyszłości.

---

## 1. Najdłuższy Wspólny Podciąg (LCS)
### Opis problemu
Dane są dwa ciągi znaków `a` i `b`. Celem jest znalezienie ich najdłuższego wspólnego podciągu, czyli sekwencji znaków, które pojawiają się w obu ciągach w tej samej kolejności, ale niekoniecznie bezpośrednio po sobie.

### Przykład
**Wejście:** `a = "adcbe"`, `b = "bdace"`

**Wyjście:**
```
Najdłuższy wspólny podciąg to: dce
```

###  Rozwiązanie dynamiczne
Tworzymy tablicę `dp` o wymiarach `(len(a) + 1) x (len(b) + 1)`, gdzie `dp[i][j]` przechowuje długość LCS dla pierwszych `i` znaków `a` i `j` znaków `b`.

**Wzór rekurencyjny:**
- Jeśli `a[i-1] == b[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`
- W przeciwnym razie: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

Rekonstrukcja rozwiązania odbywa się poprzez cofanie się po tablicy `dp` i odtwarzanie LCS.


---

## 2. Problem Plecakowy (0/1 Knapsack)
### Opis problemu
Dane jest `N` przedmiotów, każdy o wartości i wadze `(value, weight)`. Mamy plecak o maksymalnej pojemności `W` i musimy wybrać przedmioty, tak aby suma ich wartości była maksymalna oraz ich łączna waga nie przekraczała `W`.

### Rozwiązanie dynamiczne
Tworzymy tablicę `dp[i][w]`, gdzie `dp[i][w]` przechowuje maksymalną łączną wartość, jaką można osiągnąć, rozważając pierwsze `i` przedmiotów i mając plecak o pojemności `w`.

### Przykład
**Wejście:** `W = 10` `items = [(3, 2), (4, 3), (5, 4), (8, 5), (10, 9)]`

**Wyjście:**
```
Maksymalna suma wartości przedmiotów w plecaku: 15
Wybrane przedmioty:
        (3 2)
        (4 3)
        (8 5)
```


**Wzór rekurencyjny:**
- Jeśli przedmiot `i` nie mieści się w plecaku: `dp[i][w] = dp[i-1][w]`
- Jeśli przedmiot `i` mieści się: `dp[i][w] = max(dp[i-1][w], items[i-1][0] + dp[i-1][w-items[i-1][1]])`

Rekonstrukcja rozwiązania polega na sprawdzeniu, które przedmioty zostały wybrane poprzez cofanie się po tablicy `dp`.

