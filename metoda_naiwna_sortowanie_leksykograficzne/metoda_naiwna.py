def sprawdz(wzorzec, tekst):
    # algorytm sprawdza, czy występuje wzorzec w czasie O(n*k),
    # gdzie "n" to długość wzorca a "k" to długość tekstu
    n = len(wzorzec); k = len(tekst)
    for i in range(k - n + 1):  # od k-n+1 znaku nie ma sensu sprawdzać,
                                # ponieważ pozostała liczba znaków jest mniejsza niż długość wzorca
        for j in range(n): # tyle znaków musi się zgadzać
            if tekst[i + j] != wzorzec[j]: # jeśli nie ma zgodności
                break                      # to dalej nie sprawdzamy
            elif j == n - 1: # jeśli wszystkie znaki się zgadzają
                return True
    return False

tekst = input("Podaj tekst: ")
wzorzec = input("Podaj wzorzec: ")
if sprawdz(wzorzec, tekst):
    print(f"wzorzec \"{wzorzec}\" występuje w tekście \"{tekst}\"")
else:
    print(f"wzorzec \"{wzorzec}\" nie występuje w tekście \"{tekst}\"")