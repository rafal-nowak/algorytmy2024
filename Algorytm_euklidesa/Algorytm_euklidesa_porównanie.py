import time


# Niezoptymalizowany algorytm Euklidesa
def nwd_niezoptymalizowany(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# Zoptymalizowany algorytm Euklidesa
def nwd_zoptymalizowany(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Funkcja porównawcza
def porownaj_algorytmy(a, b):
    print(f"Obliczanie NWD dla liczb: {a} i {b}\n")

    # Niezoptymalizowany algorytm
    start_niezoptymalizowany = time.time()
    wynik_niezoptymalizowany = nwd_niezoptymalizowany(a, b)
    czas_niezoptymalizowany = time.time() - start_niezoptymalizowany
    print(f"Niezoptymalizowany algorytm:")
    print(f"  Wynik: {wynik_niezoptymalizowany}")
    print(f"  Czas wykonania: {czas_niezoptymalizowany:.6f} s\n")

    # Zoptymalizowany algorytm
    start_zoptymalizowany = time.time()
    wynik_zoptymalizowany = nwd_zoptymalizowany(a, b)
    czas_zoptymalizowany = time.time() - start_zoptymalizowany
    print(f"Zoptymalizowany algorytm:")
    print(f"  Wynik: {wynik_zoptymalizowany}")
    print(f"  Czas wykonania: {czas_zoptymalizowany:.6f} s\n")

    # Sprawdzenie zgodności wyników
    if wynik_niezoptymalizowany == wynik_zoptymalizowany:
        print("Oba algorytmy zwróciły ten sam wynik.")
    else:
        print("Wyniki algorytmów różnią się!")

if __name__ == '__main__':
    # Przykładowe wywołanie
    a, b = 48, 1845643
    porownaj_algorytmy(a, b)
