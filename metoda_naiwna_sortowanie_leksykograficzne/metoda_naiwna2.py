def czyWystepuje(tekst, wzorzec):
    tekst = tekst.lower()
    wzorzec = wzorzec.lower()

    for i in range(0, len(tekst)):
        j = 0;
        while (j < len(wzorzec) and tekst[i + j] == wzorzec[j]):
            j += 1
        if (j > 0 and j == len(wzorzec)):
            return True
    return False

def czyWystepujeTEST(tekst, wzorzec):
    czy_wystepuje = czyWystepuje(tekst, wzorzec)
    print(f"W tekście '{tekst}' {'występuje' if czy_wystepuje else 'nie występuje'} '{wzorzec}'")
                                      #wartość1 if warunek else wartość2

tekst = 'Metoda naiwna'
czyWystepujeTEST(tekst, 'naiwna')
czyWystepujeTEST(tekst, 'racjonalny')
czyWystepujeTEST(tekst, ' da')
czyWystepujeTEST(tekst, 'met')