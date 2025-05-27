def dziesietny_na_system(liczba, system):
    liczba = int(liczba)
    zapisanie = ''
    slownik = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    if liczba == 0:
        zapisanie = '0'

    while liczba != 0:
        reszta = liczba % system
        liczba = liczba // system
        if reszta in slownik:
            zapisanie = slownik[reszta] + zapisanie
        else:
            zapisanie = str(reszta) + zapisanie

    print(zapisanie)

def binarny_na_dziesietny (binarna,system):
    binarna = str(binarna)
    binarna = binarna[::-1]
    potega = 1

    dziesietna = 0
    for i in range(len(binarna)):
        dziesietna += int(binarna[i]) * potega
        potega = potega * system
    print(dziesietna)

binarny_na_dziesietny(1001, 2)

