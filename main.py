import math

def sito_eratostenesa(n):
    # Tworzymy listę prawda/fałsz (true dla liczb pierwszych)
    primes = [True] * (n + 1) # Zakładamy, że każda liczba jest pierwszą
    primes[0] = False
    primes[1] = False  # Odrzucamy 0 i 1, bo nie są liczbami pierwszymi

    for x in range(2, int(math.sqrt(n)) + 1):
        if primes[x]:
            for j in range(x * x, n + 1, x): # Odrzucamy wielokrotności x
                primes[j] = False

    for i in range(n + 1):
      if primes[i]:
        print(i)

if __name__ == "__main__":
    n = int(input("Podaj górną granicę zakresu: "))
    sito_eratostenesa(n)
