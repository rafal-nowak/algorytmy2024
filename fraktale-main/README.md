# Rekurencyjnego tworzenia fraktali: zbiór Cantora, drzewo binarne, dywan Sierpińskiego, płatek Kocha.
## Co to jest fraktal?
  to obiekt składający się z coraz bardziej złożonych detali, z których każdy jest podobny do całości. Podczas tworzenia fraktali w języku python bedziemy uzywać modułu Turtle.
## Turtle
Moduł turtle w Pythonie pozwala na tworzenie grafiki wektorowej za pomocą prostych poleceń sterujących wirtualnym "żółwiem". Użytkownicy mogą rysować linie, figury geometryczne i animacje, zmieniając kolory, kształty i kierunki żółwia. Jest to narzędzie często wykorzystywane w edukacji do nauki programowania i wizualizacji algorytmów.
## Dywan Sierpińskiego
Dywan Sierpińskiego otrzymujemy z kwadratu przez podzielenie go na dziewięć mniejszych kwadratów (3 x 3). Następnie środkowy kwadrat zostaje zamalowany. Ponownie rekurencyjnie wywołujemy tę funkcję dla każdego z pozostałych kwadratów.

![image](https://github.com/user-attachments/assets/4fe4585e-78b0-42fe-8b0b-d7d6dc252f04)
### funkcja
```python
def kwadrat(bok, kolor):
        z.color(kolor)
        z.begin_fill()
        for i in range(4):
            z.forward(bok)
            z.right(90)
        z.end_fill()

    if stopien == 0:
        kwadrat(dl_bok, 'black')
        return None
    else:
        kwadrat(dl_bok, 'white')
        for i in range(4):
            for j in range(2):
                dywan_sierpinskiego(z, stopien-1, dl_bok/3)
                z.forward(dl_bok/3)
            z.forward(dl_bok/3)
            z.right(90)
```

## Zbiór Cantora
Zbiór Cantora tworzymy, zaczynając od odcinka, z którego usuwamy środkową część, pozostawiając jedynie jego pierwszy i trzeci fragment. Następnie ten sam proces powtarzamy dla każdego z pozostałych odcinków. W każdym kolejnym kroku liczba odcinków podwaja się, a ich długość maleje. Jeśli narysujemy kolejne etapy jeden pod drugim, powstanie układ o strukturze fraktalnej.

![image](https://github.com/user-attachments/assets/baecdd09-a27d-46c6-9881-5817cc16b9e5)
### funkcja
```python
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
```
## Płatek Kocha
Płatek Kocha tworzy się poprzez podzielenie odcinka na trzy równe części, usunięcie środkowej i zastąpienie jej trójkątem równobocznym, którego boki mają długość równą usuniętemu odcinkowi. Proces ten powtarza się dla każdego powstałego fragmentu odcinka bazowego, a następnie dla każdego fragmentu nowo utworzonych odcinków. W wyniku tego podziału figura staje się coraz bardziej złożona, a jej długość rośnie w nieskończoność, ponieważ każdy etap zwiększa liczbę odcinków czterokrotnie.

![image](https://github.com/user-attachments/assets/1834928b-7695-4d92-a1b6-b55d2cbe1511)
### funkcja
```python
def platek_kocha(z, stopien, dl_bok):

    def bok(stopien, dl_bok):
        if stopien == 0:
            z.forward(dl_bok)
        else:
            bok(stopien-1, dl_bok/3)
            z.left(60)
            bok(stopien-1, dl_bok/3)
            z.right(120)
            bok(stopien-1, dl_bok/3)
            z.left(60)
            bok(stopien-1, dl_bok/3)

    z.right(30)
    for i in range(3):
        bok(stopien, dl_bok)
        z.right(120)

    z.left(30)
```
## Drzewo Binarne
Drzewo binarne tworzy się z odcinka, który rozdziela się na dwa kolejne, skierowane pod kątem 45 stopni w lewo i w prawo. Powtarzając ten proces dla każdego nowego odcinka, uzyskujemy strukturę przypominającą „koronę drzewa”.

![image](https://github.com/user-attachments/assets/2c0b877a-2dc1-4a35-8a52-2a9071fe8a7f)
### funkcja
```python
   def drzewo_binarne(z, stopien, dl_bok):
      if stopien == 0:
          pozycja = z.pos()
          z.forward(dl_bok)
          z.goto(pozycja)
      else:
          pozycja = z.pos()
          z.forward(dl_bok)
          z.left(45)
          drzewo_binarne(z, stopien-1, dl_bok/2)
          z.right(90)
          drzewo_binarne(z, stopien-1, dl_bok/2)
          z.left(45)
          z.goto(pozycja)
  ```
  






