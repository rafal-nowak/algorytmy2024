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
    liczba = str(liczba)[::-1]  # Odwracamy liczbę, aby ułatwić mnożenie wg potęg
    potega = 1  # Pierwsza potęga systemu
    slownik = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}  # Szesnastkowe cyfry
    dziesietna = 0  # Wynik konwersji
    
    for i in range(len(liczba)):
        if liczba[i] in slownik:
            dziesietna += slownik[liczba[i]] * potega
        else:
            dziesietna += int(liczba[i]) * potega
        potega *= system  # Zwiększamy potęgę systemu
    
    print(dziesietna)

# Przykładowe użycie:
system_na_dziesietny("fe80", 16)  # Wynik: 65152
```

### Jak to działa?
1. Odwracamy liczbę, ponieważ konwersja wymaga mnożenia wg potęg.
2. Tworzymy słownik zamieniający litery na odpowiadające im wartości dziesiętne.
3. Przechodzimy przez każdą cyfrę liczby:
   - Jeśli jest literą, pobieramy wartość ze słownika.
   - Jeśli jest cyfrą, konwertujemy na liczbę.
   - Mnożymy przez aktualną potęgę systemu i dodajemy do wyniku.
4. Wynik drukujemy na ekranie.

---

## 3. Konwersja dziesiętnej na dowolny system
### Funkcja:
```python
def dziesietny_na_system(liczba, system):
    liczba = int(liczba)
    zapisanie = ''
    slownik = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    
    while liczba != 0:
        reszta = liczba % system  # Obliczamy resztę z dzielenia
        liczba = liczba // system  # Dzielimy liczbę przez system
        
        if reszta in slownik:
            zapisanie += slownik[reszta]
        else:
            zapisanie += str(reszta)
    
    zapisanie = zapisanie[::-1]  # Odwracamy wynik
    print(zapisanie)

# Przykładowe użycie:
dziesietny_na_system(16, 2)  # Wynik: 10000
```

### Jak to działa?
1. Pobieramy liczbę i zamieniamy na `int`, jeśli potrzeba. .
2. Dzielimy liczbę przez system, zapisując resztę:
   - Jeśli reszta to liczba od 10 do 15, zamieniamy na odpowiadającą literę.
   - W przeciwnym razie zapisujemy wartość jako cyfrę.
3. Odwracamy wynik, aby uzyskać poprawny zapis liczby w nowym systemie.

---

