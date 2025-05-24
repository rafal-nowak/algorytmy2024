# Konwersja systemów liczbowych w Pythonie

## 1. Gotowe funkcje w Pythonie do zmiany systemów liczbowych
Python posiada wbudowane funkcje umożliwiające operowanie między systemami liczbowymi.

- `bin(liczba)` – zamienia liczbę na system binarny
- `oct(liczba)` – zamienia liczbę na system oktalny
- `hex(liczba)` – zamienia liczbę na system szesnastkowy
- `int(liczba, system)` – konwertuje liczbę z podanego systemu na dziesiętny

### Przykłady:
```python
print(bin(10))  # Wynik: 0b1010
print(oct(10))  # Wynik: 0o12
print(hex(10))  # Wynik: 0xa
print(int("1010", 2))  # Wynik: 10
```

Jednak po co ułatwiać sobie życie skoro możemy również napisać własne funkcje!

---

## 2. Konwersja dowolnego systemu na dziesiętny
### Funkcja:
```python
def system_na_dziesietny(liczba, system):
    liczba = str(liczba).lower()[::-1]
    potega = 1
    slownik = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    dziesietna = 0

    for i in range(len(liczba)):
        if liczba[i] in slownik:
            dziesietna += slownik[liczba[i]] * potega
        else:
            dziesietna += int(liczba[i]) * potega
        potega *= system

    return dziesietna


# Przykładowe użycie:
system_na_dziesietny("fe80", 16)  # Wynik: 65152
```

### Jak to działa?
1. Odwracamy liczbę, aby najniższe cyfry przetwarzać jako pierwsze.
2. Dla każdej cyfry:
- Zamieniamy litery (a–f) na odpowiadające liczby (jeśli system > 10).
- Inne znaki zamieniamy na liczby całkowite.
- Mnożymy wartość przez odpowiednią potęgę systemu i dodajemy do sumy.
- Zwiększamy potęgę w każdej iteracji.
- Zwracamy wynik w systemie dziesiętnym.

---

## 3. Konwersja dziesiętnej na dowolny system
### Funkcja:
```python
def dziesietny_na_system(liczba, system):
    liczba = int(liczba)
    zapisanie = ''
    slownik = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    if liczba == 0:
        return '0'

    while liczba != 0:
        reszta = liczba % system
        liczba = liczba // system

        if reszta in slownik:
            zapisanie += slownik[reszta]
        else:
            zapisanie += str(reszta)

    return zapisanie[::-1]


# Przykładowe użycie:
dziesietny_na_system(16, 2)  # Wynik: 10000
```

### Jak to działa?
- Dzielimy liczbę przez system docelowy i zapisujemy reszty.
- Dla wartości 10-15 stosujemy litery (a-f).
- Wynik odwracamy, aby uzyskać poprawny zapis w systemie docelowym.

### Zadania
Zamień liczbę 3E8A z systemu szesnastkowego (16) na system piątkowy (5).
Zamień liczbę 101101 z systemu binarnego (2) na system ósemkowy (8).
Zamień liczbę 1100101 z systemu binarnego (2) na system piętnastkowy (15).
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

przykladowe rozwiazanie 
Zadanie 1: 3E8A (system 16) → system 5
dziesietna1 = system_na_dziesietny("3E8A", 16)
wynik1 = dziesietny_na_system(dziesietna1, 5)
print(f"3E8A (16) = {wynik1} (5)")

Zadanie 2: 101101 (system 2) → system 8
dziesietna2 = system_na_dziesietny("101101", 2)
wynik2 = dziesietny_na_system(dziesietna2, 8)
print(f"101101 (2) = {wynik2} (8)")

Zadanie 3: 1100101 (system 2) → system 15
dziesietna3 = system_na_dziesietny("1100101", 2)
wynik3 = dziesietny_na_system(dziesietna3, 15)
print(f"1100101 (2) = {wynik3} (15)")



---

