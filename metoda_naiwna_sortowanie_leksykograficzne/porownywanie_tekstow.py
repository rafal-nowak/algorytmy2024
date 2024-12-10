
wyraz1 = "Arbuz"
wyraz2 = "ArbuZ"

lista1 = ["Polska", "Hiszpania", "Argentyna"]
lista2 = ["Polska", "Chiszpania", "Arkentyna"]
def takie_same(tekst1,tekst2):
    if len(tekst1) != len(tekst2):
        return False

    for i in range(len(tekst1)):
        if tekst1[i] != tekst2[i]:
        # if tekst1[i].lower() != tekst2[i].lower():
            return False
    return True

print(takie_same(wyraz1, wyraz2))

for i in range(len(lista1)):
    if takie_same(lista1[i],lista2[i]):
        print(f"Wyraz {lista1[i]} jest taki sam jak {lista2[i]}")
    else:
        print(f"Wyraz {lista1[i]} nie jest taki sam jak {lista2[i]}")


# Nie trzeba również tworzyć funkcji, wystarczy np.
# if wyraz1 == wyraz2:
#   ...
#if lista1[i] == lista2[i]:
#   ...