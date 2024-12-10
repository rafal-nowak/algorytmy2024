slowa = ["pies", "babcia", "agrafke", "banan"]

def porownaj(slowo1, slowo2):
    return slowo1 > slowo2

# Srtowanie bąbelkowe
def sortowanie_leksykograficzne(slowa):
    n = len(slowa)
    for i in range(n):
        for j in range(0, n-i-1):
            if porownaj(slowa[j], slowa[j+1]):
                slowa[j], slowa[j+1] = slowa[j+1], slowa[j]  # Zamiana miejscami

sortowanie_leksykograficzne(slowa)

print(slowa)


"""
slowa = ["banan", "baba", "brzoza", "bilet"]

# Sortowanie leksykograficzne
posortowane_slowa = sorted(slowa)

print(posortowane_slowa)
"""