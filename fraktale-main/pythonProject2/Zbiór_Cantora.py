def zbior_cantora(z, dlugosc_linii, wyciecie, liczba_linii):
    if liczba_linii == 0:
        z.pd()
        z.fd(dlugosc_linii)
        z.pu()
    else:
        nowa_dlugosc = dlugosc_linii * (1-wyciecie)/2
        zbior_cantora(z, nowa_dlugosc, wyciecie, liczba_linii -1)
        z.fd(dlugosc_linii * wyciecie)
        zbior_cantora(z, nowa_dlugosc, wyciecie, liczba_linii -1)


def fraktal_cantora(z, dlugosc_lini, ile):
    for i in range(ile):
        zbior_cantora(z, dlugosc_lini, 1/3, i)
        z.back(dlugosc_lini)
        z.lt(90)
        z.back(100 / ile - 1)
        z.rt(90)