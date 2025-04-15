# Schemat Hornera

Implementacja algorytmu Hornera w języku Python.

## 1. Czym jest schemat Hornera?

Schemat Hornera jest to wspolna nazwa dla dwóch algorytmów

-Algorytmu dzielenia wielomianu przez dwumian liniowy

-Algorytmu obliczania wartości dowolnego wielomianu o jednej zmiennej

### Postać wielomianu

Wielomian w postaci ogólnej:

$`
P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0
`$

W schemacie Hornera przekształcany jest do postaci:

$P(x) = (\dots((a_n x + a_{n-1})x + a_{n-2})x + \dots + a_1)x + a_0$

## 2.Przykład zastosowania schematu Hornera:
Dany jest wielomian: $W\left( x \right)=4x^{3}+2x^{2}-5x+20$

$W\left( x \right) = x\left(  4x^{2}+2x-5\right)+20$

$W\left( x \right) = x\left(  x\left( 4x+2 \right)-5\right)+20$

$W\left( 2 \right) = 2\left(  2\left( 4\cdot 2+2 \right)-5\right)+20$

$W\left( 2 \right) = 2\left(  2\left( 8+2 \right)-5\right)+20$

$W\left( 2 \right) = 2\left(  2\cdot20-5\right)+20$

$W\left( 2 \right) = 2\left(  15\right)+20$

$W\left( 2 \right) = 30+20=50$

## 3. Zadania:

1. Za pomocą schematu Hornera oblicz wartość wielomianu $W\left( x \right)=4x^{3}+5x^{2}+3x-7$ dla x = 3

2. Podziel wielomian $W\left( x \right)=6x^{3}-4x^{2}+7x-22$ przez dwumian $W\left( x \right)=x-3$

## 4. Implementacja algorytmu w Pythonie

### Obliczanie wartości wielomianu

```python
def horner(coefficients, x):
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result
```
### Dzielenie wielomianu:

```python
def horner_division(coefficients, c):
    n = len(coefficients)
    quotient = [0] * (n - 1)
    remainder = coefficients[0]
    for i in range(1, n):
        quotient[i - 1] = remainder
        remainder = remainder * c + coefficients[i]
    return quotient, remainder
```
### Dzielenie przez wielomian:
```python
coefficients = [4, -3, 1, 2, -5]
c = 2
quotient, remainder = horner_division(coefficients, c)
print("Quotient:", quotient)  # Wynik: [4, 5, 11, 24]
print("Remainder:", remainder)  # Wynik: 43

