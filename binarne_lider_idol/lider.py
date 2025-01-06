zbior = [1, 3, 3, 2, 5, 5, 3, 3, 3, 3, 1]
lider = zbior[0]
n = 1
for i in range(1,len(zbior)):
    if n > 0:
        if lider == zbior[i]:
            n = n + 1
        else:
            n = n - 1
    else:
        lider = zbior[i]
        n = 1

if n == 0:
    print("Zbiór nie ma lidera")
    exit()

liczba_wystapien_lidera = 0
for i in range(0,len(zbior)):
    if zbior[i] == lider:
        liczba_wystapien_lidera += 1

if liczba_wystapien_lidera > len(zbior) / 2:
    print("Liderem zbioru jest ",lider)
else:
    print("Zbiór nie ma lidera")