# Algorytmy Zachłanne
## Definicja
***Algorytm zachłanny*** - algorytm który w każdym kolejnym kroku dokonuje wyboru lokalnie optymalnego. Rozwiązanie zachłanne zawsze wybiera najlepszą z dostępnych opcji nie sprawdzając dalszych możliwości, co czasem powoduje uzyskanie rozwiązania nieoptymalnego globalnie
## Zasada działania algorytmu zachłannego
Algorytm zachłanny zawsze wybiera najlepszą lokalnie możliwą opcję, można to łatwo zaprezentować na przykładzie piramidy
![](https://cdn.discordapp.com/attachments/1047076190063697940/1310674267008143480/1004.p1.png?ex=67461408&is=6744c288&hm=16ff1b4f54bb0ea1b17110f1693cc78062400b183d5728dbf971ec71ec52c2e6&)
Algorytm zaczyna na samym szczycie piramidy wybierając jedno z pól znajdujących się bezpośrednio pod nim. Nasz algorytm otrzymał za zadanie znaleźć największą sumę wartości w poniższych polach. Zasada działania algorytmu wygląda tak:
```mermaid
graph TD
A[Koniec piramidy?] -- Tak --> B(Koniec programu)
A -- Nie --> C[Pole Lewe > Pole Prawe?]
C -- Tak --> E(sum=+PoleLewe)
C -- Nie --> F(sum=+PolePrawe)
E-->G(powtórz algorytm)
F-->G
G-->A
```
***
***Zad1.1***
Podaj sumę którą obliczy nasz algorytm.
***
![](https://cdn.discordapp.com/attachments/1047076190063697940/1310674468229615658/1004.p6-removebg-preview.png?ex=67461438&is=6744c2b8&hm=700a1364a0eb5a7056577ca54e3e803c267be945678d300850dfefee199b2ef4&)
Suma wynosi ==19==
***
***Zad1.2***
Czy otrzymana suma jest największą możliwą wartością?
***
### Probem naszego rozwiązania
W przedstawionym roziązaniu problemu wykorzystano algorytm zachłanny, który wybierając rozwiązania optymalne lokalnie, nie uzyskał rozwiązania optymalnego globalnie
**Rozwiązanie zachłanne daje nam wynik ==19== kiedy rozwiązaniem optymalnym jest wynik ==26==**

![](https://cdn.discordapp.com/attachments/1047076190063697940/1310677103683043328/1004.p7.png?ex=674616ac&is=6744c52c&hm=4ac9b489b79b350f2bc4ec244ce77dd57cbb19d0fe93d531f2de6128f57a269c&)

## Problem wydawania reszty
Problem wydawania reszty jest ciekawym zastosowaniem algorytmu zachłannego, ponieważ to, czy otrzymamy rozwiązanie optymalne globalnie zależy od otrzymanego zestawu nominałów. Aby nasz przykład był prosty i dawał nam optymalne rozwiązania przyjmijmy że nominały którymi dysponujemy to 1$ 2$ i 5$.

Algorytm na wejściu przyjmuje tylko jedną wartość jaką jest reszta do wydania, na wyjściu otrzymujemy ilość monet użytych do wydania reszty
```mermaid
graph LR
A[Reszta>=5?] -- Tak --> B(Reszta=-5, count=+1)
B -->A
A --Nie--> C[Reszta>=2?]
C --Tak--> D(Reszta=-2, count=+1)
D-->C
C--Nie-->E[Reszta>=1?]
E--Nie-->G(Koniec programu)
E--Tak-->F(Reszta=-1, count=+1)
F-->E

```
 ***
***Zadanie 2.1***
Mamy do wydania resztę 13 $, jaka jest najmniejsza liczba monet które należy użyć, aby wydać tą resztę?
***
### Przykładowa implementacja rozwiązania
```python
def change():  
  
    # User input  
  try:  
        Change = int(input("Enter change: "))  
        n = int(input("Amount of different coins: "))  
        Coins = []  
        for a in range(n):  
            Coins.append(int(input(f"Value of coin {a + 1}: ")))  
    except:  #If user input is other than number
        print("Something went wrong, make sure you used correct values and try again")  
        exit(1)  
  
    Coins.sort(reverse=True) #Sorting our coins descending
  
  i = 0  
  counter = 0  
  
  if(Coins[0]>Change):
        print("Coins values are greater than change, giving change is impossible")  
        exit(1)  
    while Change > 0: #counting coins  
  while Change >= Coins[i]:  
            Change -= Coins[i]  
            counter+=1  
  i += 1  
  
  print(f"Required amount of coins:{counter}") #result  
  
if __name__ == '__main__':  
    change()
```
***
***Zad2.2***
Sprawdź co się stanie po wprowadzeniu wartości:
Reszta=30
Nominały=21,10,1
Czy powstałe rozwiązanie jest rozwiązaniem optymalnym?
***
***Zad2.3***
Dodaj możliwość wyświetlenia jakie nominały zostały użyte do wydania reszty
***
***Zad2.4***
Jeżeli nasz algorytm nie jest w stanie wydać reszty z powodu niedostępnych nominałów otrzymujemy błąd, dodaj proste zabezpieczenie w przypadku gdy wydanie reszty jest niemożliwe
***
## Inne przykładowe zastosowania algorytmów zachłannych

- optymalizacja zasobów (np. problem plecakowy)
-   nawigacja i znajdowanie najkrótszej ścieżki (np. algorytm Dijkstry)
-   kompresja danych (np. kodowanie Huffmana)
-   harmonogramowanie zadań (np. problem najwcześniejszego terminu)

