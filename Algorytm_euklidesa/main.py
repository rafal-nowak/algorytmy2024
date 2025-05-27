def iteracyjna_odejmowanie(a, b):
    c = a
    d = b
    while a!=b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    print(f"Najwiekszy wspolny dzielnik liczb {c} oraz {d} wynosi: {a} \n")

def rekurencyjna_odejmowanie(a, b):
    d = a
    e = b
    if a != b:
        if a > b:
            return rekurencyjna_odejmowanie(a - b, b)
        else:
            return rekurencyjna_odejmowanie(a, b - a)
    return a

def iteracyjna_zoptymalizowana(a, b):
    c = a
    d = b
    temp = 0
    while b != 0:
        temp = b
        b = a % b
        a = temp
    print(f"Najwiekszy wspolny dzielnik liczb {c} oraz {d} wynosi: {a} \n")

def nww_euklides(a, b):
    nww = 0
    c = a
    d = b
    while a!=b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    nww = int(c * d / a)
    print(f"Najmniejsza wspolna wielokrotnosc liczb {c} oraz {d} wynosi: {nww} \n")

if __name__ == '__main__':
    print("ALGORYTM EUKLIDESA \n")
    a = int(input("Podaj pierwsza liczbe naturalna: \n"))
    b = int(input("Podaj druga liczbe naturalna: \n"))
    choice = 0

    print("OPCJE: \n")
    print("1. Algorytm Euklidesa w wersji iteracyjnej z odejmowaniem \n")
    print("2. Algorytm Euklidesa w wersji rekurencyjnej z odejmowaniem \n")
    print("3. Algorytm Euklidesa w wersji iteracyjnej zoptymalizowanej z odejmowaniem \n")
    print("4. Obliczanie NWW dwoch liczb naturalnych z wykorzystaniem algorytmu Euklidesa \n")
    choice = int(input("Wybierz jedna z powyzszych opcji \n"))

    if choice == 1:
        iteracyjna_odejmowanie(a, b)
    elif choice == 2:
        nwd = rekurencyjna_odejmowanie(a, b)
        print(f"Najwiekszy wspolny dzielnik liczb {a} oraz {b} wynosi: {nwd} \n")
    elif choice == 3:
        iteracyjna_zoptymalizowana(a, b)
    elif choice == 4:
        nww_euklides(a, b)


