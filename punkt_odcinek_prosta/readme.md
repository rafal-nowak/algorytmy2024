# Badanie położenia punktu względem prostej i przynależności punktu do odcinka

## 1. Definicje 
Położenie punktu, odcinka czy prostej określamy na płaszczyźnie kartezjańskiej.  

### PŁASZCZYZNA KARTEZJAŃSKA
*Płaszczyzna kartezjańska* to dwuwymiarowa płaszczyzna współrzędnych utworzona przez **przecięcie dwóch prostopadłych linii**. Linia pozioma jest znana jako **```oś OX```**, a linia pionowa jako **```oś OY```**.

### PUNKT
Położenie *punktu* wyznaczamy za pomocą **liczbowych wartości jego współrzędnych x i y** - **```P(x, y)```** - które odpowiednio odnoszą się do osi poziomej OX i osi pionowej OY. 


### ODCINEK
*Odcinek* to część prostej zawarta **pomiędzy dwoma punktami** tej prostej, z tymi punktami włącznie. Współrzędne jego krańców odpowiadają współrzędnym ograniczających go punktów. 

### PROSTA
*Prosta* to krzywa na płaszczyźnie zawierająca w sobie **zbiór punktów** o współrzędnych **spełniających pewne równanie**. Jest ona nieograniczona z żadnej strony. 
Równanie prostej może być zapisane w postaci: 
- **ogólnej** --->   **```0 = Ax + By + C```**,

    gdzie **A**, **B** i **C** są liczbami rzeczywistymi i **A^2 + B^2 ≠ 0**

- **kanonicznej (kierunkowej)** --->   **```y = ax + b```**,

    gdzie **a** jest współczynnikiem kierunkowych i określa kąt nachylenia prostej względem osi OX, a wyraz wolny **b** wyznacza punkt przecięcia prostej z osią OY


## 2. Badanie położenia punktu względem prostej 
Istnieją dwie opcje położenia punktu względem prostej – albo on do niej należy albo nie. 

Żeby sprawdzić, która z opcji jest właściwa dla danych prostej i punktu, trzeba: 

### Wersja A 
podstawić współrzędne punktu **```P(x, y)```** do równania prostej, najlepiej tego w postaci kierunkowej **```k: y = ax + b```**. 
Jeżeli po przyrównaniu wartości obu stron równania zachodzi **TOŻSAMOŚĆ**, punkt należy do prostej.

python 
 
```python
def is_in_line_1(x, y, a, b):
    if(y == a*x + b):
        return("Punkt należy do prostej")
    else:
        return("Punkt nie należy do prostej")
```

C++
```c++
#include <iostream> 
using namespace std; 
int main() 
{
int a, b, x, y; 
cout<< „Podaj a i b równania prostej”<<endl; 
cin>>a>>b; 
cout<<endl<< „Podaj x i y punktu A”<<endl; 
cin>>x>>y; 
if (y==a*x+b) cout<<endl<< „Punkt nalezy do prostej”; 
else cout<<endl<<„Punkt nie nalezy do prostej";
}
```


### Wersja B
podstawić współrzędne punktu i dwóch innych punktów należących do prostej do wzoru 
**```(y-yA)(xB-xA)-(x-xA)(yB-yA) = 0```**.
Jeżeli po przyrównaniu wartości obu stron równania zachodzi **TOŻSAMOŚĆ**, punkt należy do prostej.

python 
```python
def is_in_line_2(x, y, xa, ya, xb, yb):
    if((y-ya)*(xb-xa)-(x-xa)*(yb-ya) == 0):
        return("Punkt należy do prostej")
    else:
        return("Punkt nie należy do prostej")
```

C++
```c++
#include <iostream> 
using namespace std; 
int main() 
{
int x, y, xA, yA, xB, yB; 
cout<< „Podaj wspolrzedne x i y punktu”<<endl; 
cin>>x>>y; 
cout<<endl<< „Podaj xA i yA jednego z koncow odcinka”<<endl; 
cin>>xA>>yA;
cout<<endl<< „Podaj xB i yB drugiego z koncow odcinka”<<endl; 
cin>>xB>>yB; 
if ((y-yA)*(xB-xA)-(x-xA)*(yB-yA) == 0) cout<<endl<< „Punkt nalezy do prostej”; 
else cout<<endl<<„Punkt nie nalezy do prostej";
}
```

## 3. Badanie przynależności punktu do odcinka 
Sprawdzając czy na płaszczyźnie kartezjańskiej punkt należy do odcinka należy: 
1.	Pobrać **współrzędne danego punktu**
2.	Pobrać **współrzędne 2 punktów** ograniczających ten odcinek
3.	Sprawdzić czy **punkt należy do prostej** według wzoru na prostą przechodzącą przez trzy punkty **```(y-yA)(xB-xA)-(x-xA)(yB-yA) = 0```** (funkcja wcześniej)
4.	Jeśli punkt należy do prostej, sprawdzić czy **spełnione są warunki** **```XC >= min(XA ; XB), XC <= max(XA ; XB) oraz YC >= min(YA ; YB), YC <= max(YA ; YB) ```**
5.	Jeśli **wszystkie warunki** są **spełnione** to ***PUNKT NALEŻY DO ODCINKA***.

```python
def is_in_segment(x, y, xa, ya, xb, yb):
    if((y-ya)*(xb-xa)-(x-xa)*(yb-ya) == 0):
        x_minimum = min(xa, xb)
        y_minimum = min(ya, yb)
        x_maksimum = max(xa,xb)
        y_maksimum = max(ya, yb)
        if (x>=x_minimum and x<=x_maksimum and y>=y_minimum and y<=y_maksimum):
            return("Punkt należy do odcinka")
    else:
        return("Punkt nie należy do odcinka")
```


## 4. Zadania 
1. Sprawdź czy: 
   * punkt A(1, 2) należy do prostej l: y = x + 1
   * punkt B(4,7) należy do odcinka ograniczonego punktami S(2, 5) i R(9, 6).
2. Napisz kod, ktory sprawdza czy wprowadzone przez użytkownika dane są liczbami.
3. Napisz funkcję, która sprawdza przynależność punktu do prostej na podstawie równania prostej W POSTACI OGÓLNEJ.
4. Napisz funkcję, która obliczy odległość punktu P(x,y) od prostej k: 0 = Ax + By + C.

## Źródła 
https://wlasnoscigeometryczne.wordpress.com/badanie-polozenia-punktu-wzgledem-prostej/

https://pl.wikipedia.org/wiki/Prosta

https://algorytm.htw.pl/

https://wlasnoscigeometryczne.wordpress.com/przynaleznosc-punktu-do-prostej/
