def divide_polynomials(dividend, divisor):
    """
    Dzieli wielomian dividend przez divisor.
    Zwraca iloraz i resztę.

    dividend: lista współczynników wielomianu dzielnego (od najwyższego stopnia)
    divisor: lista współczynników wielomianu dzielnika (od najwyższego stopnia)
    """
    # Stopnie wielomianów
    n = len(dividend) - 1
    m = len(divisor) - 1

    # Inicjalizujemy iloraz jako wielomian zerowy o stopniu (n - m)
    quotient = [0] * (n - m + 1)

    # Tworzymy kopię dzielnej, aby móc na niej operować
    remainder = dividend[:]

    # Główna pętla dzielenia
    for i in range(n - m + 1):
        # Obliczamy współczynnik ilorazu (główny współczynnik podzielonej)
        quotient[i] = remainder[i] / divisor[0]

        # Aktualizujemy resztę, odejmując iloraz * dzielnik
        for j in range(m + 1):
            remainder[i + j] -= quotient[i] * divisor[j]

    # Reszta powinna mieć stopień mniejszy niż dzielnik
    remainder = remainder[-(m):]  # Zwracamy tylko część reszty, która się liczy

    return quotient, remainder


# Przykład użycia:
dividend = [1,12, -3, 7]  # x^2 - 3x + 2
divisor = [7, 9]  # x - 1

quotient, remainder = divide_polynomials(dividend, divisor)
print("Iloraz:", quotient)
print("Reszta:", remainder)
