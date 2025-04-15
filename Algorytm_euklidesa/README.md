# Algorytm Euklidesa

## 1. Czym jest Algorytm Euklidesa?
Algorytm Euklidesa został opisany przez starożytnego greckiego matematyka Euklidesa w dziele "Elementy". Służy do wyznaczania największego wspólnego dzielnika (NWD) dwóch liczb naturalnych.

## 2. Złożoność Algorytmu Euklidesa
- Złożoność czasowa: `O( log(m + n) )`
- Złożoność pamięciowa: `O(1)`
  
## 3. Zastosowania Algorytmu Euklidesa
- Generowanie rytmów w muzyce
- Wykorzystanie w algorytmie RSA
- Wykorzystanie w rozkładzie na czynniki liczb całkowitych
  
## 4. Kroki Algorytmu Euklidesa opartego na odejmowaniu
Poniższe czynności wykonujemy dopóki obie dane liczby naturalne nie będą sobie równe:
- Sprawdź, która z liczb jest większa
- Wykonaj odejmowanie mniejszej liczby od większej
- Zastąp większą liczbę wynikiem powyższego odejmowania

W momencie, gdy obie liczby się zrównają to jedna z nich jest wyznaczonym największym wspólnym dzielnikiem (NWD).

## 5. Zastosowanie Algorytmu Euklidesa w programowaniu (wersja iteracyjna)
![Zrzut ekranu 2024-12-01 152936](https://github.com/user-attachments/assets/52a963f3-3d85-4457-b6f8-0d99c1a85d71)

## 6. Zastosowanie Algorytmu Euklidesa w programowaniu (wersja rekurencyjna)
![image](https://github.com/user-attachments/assets/6bab8345-126d-46cf-bcc8-d962243eb57a)

## 7. Zastosowanie Algorytmu Euklidesa w programowaniu (wersja zoptymalizowana)
![image](https://github.com/user-attachments/assets/1341a2b5-4de8-42ea-a3ef-ead103ee20ad)

## 8. Wzór na NWW (najmniejszą wspólną wielokrotność) w oparciu o wyznaczenie NWD
`a * b / NWD(a, b)`

## 9. Ćwiczenie
Wyznacz NWD liczb 1989 oraz 867. W rozwiązaniu wykorzystaj algorytm Euklidesa.

Poprawna odpowiedź: 51

## 10. Dowód poprawności Algorytmu Euklidesa
Teza: 

  NWD(a, b) = NWD(b, a mod b)
  
Założenia:

  d = NWD(a, b), zatem a = sd, b = td
  
  r = a mod b, zatem a = pb + r
  
  gdzie p, s oraz t należą do zbioru liczb całkowitych
  
Dowód:

  r = a - pb = sd - ptd = d(s - pt)
  
Wniosek: d jest dzielnikiem liczb a mod b oraz NWD(a, b).
  
