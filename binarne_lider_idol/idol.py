macierz = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]

for i in range(len(macierz)):
    if macierz[i] == [0]*len(macierz):
        for x in macierz[:i] + macierz[i+1:]:
            if x[i] == 0:
                print("Zbior nie ma idola")
                break
        else:
            print(f"Idol to {i}")
        break
else:
    print("Zbior nie ma idola")