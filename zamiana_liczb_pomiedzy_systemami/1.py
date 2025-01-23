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
