def dziesietny_na_system(liczba, system):
    liczba = int(liczba)
    zapisanie = ''
    while liczba != 0:
        reszta = liczba % system
        liczba = liczba // system
        zapisanie = zapisanie + str(reszta)
    zapisanie = zapisanie[::-1]
    print(zapisanie)


dziesietny_na_system(16, 2)
