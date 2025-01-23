def system_na_dziesietny (liczba,system):
    liczba = str(liczba)
    liczba = liczba[::-1]
    potega = 1
    slownik = {'a': 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    dziesietna = 0
    for i in range(len(liczba)):
        if liczba[i] in slownik:
            dziesietna += int(slownik[liczba[i]]) * potega
        else:
            dziesietna += int(liczba[i]) * potega
        potega = potega * system
    print(dziesietna)


system_na_dziesietny("fe80", 16)
