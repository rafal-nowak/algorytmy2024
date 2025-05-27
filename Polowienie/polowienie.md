# Znajdowanie miejsca zerowego metodą połowienia przedziałów (metoda Bisekcji)

## 1. Czym jest metoda połowienia?

Metoda połowienia, znana również jako metoda bisekcji, to numeryczna metoda znajdowania pierwiastków funkcji. Jest to jedna z najprostszych i najstarszych metod numerycznych stosowanych do rozwiązywania równań nieliniowych. Można ją porównać do wyszukiwania binarnego, lecz zamiast znajdywania danej liczby w posortowanym zbiorze, staramy się oszacować wartość pierwiastka w danym przedziale z założoną dokładnością.

Aby móc zastosować algorytm należy najpierw zdefiniować przedział $[a, b]$, w którym analizowana przez nas funkcja $f(x)$ spełnia poniższe warunki:
- **Ciągłość funkcji:** Funkcja $f(x)$ musi być ciągła w przedziale $[a, b]$. W dużym uproszczeniu oznacza to, że jesteśmy w stanie narysować jej wykres nie odrywając ołówka od kartki.
- Funkcja $f(x)$ na krańcach przedziału $[a,b]$ przyjmuje **różne znaki** ( $f(a) * f(b) < 0$ ).

Gdy funkcja $f(x)$ spełnia powyższe trzy warunki, to w przedziale [a,b] zagwarantowane jest istnienie pierwiastka i możemy go wyszukać algorytmem połowienia (bisekcji).

## 2. Działanie algorytmu

#### 1. Wyznaczamy punkt $x_o$ jako środek przedziału $[a,b]$ zgodnie ze wzorem:

$$x_0 = \frac{a+b}{2}$$

#### 2. Obliczamy wartość funkcji w punkcie $x_0$. 

#### 3. Sprawdzamy, czy $x_0$ jest pierwiastkiem.

- Jeśli długość przedziału ($|b-a|$) jest mniejsza od założonej dokładności wyliczeń pierwiastka ( $\epsilon$ ), to wartość $x_0$ jest poszukiwanym przybliżeniem. Kończymy algorytm.
- W przeciwnym razie sprawdzamy, czy $f(x_0)$ znajduje się dostatecznie blisko 0:
  
$$| f(x)| < \epsilon$$
  
- Jeśli nierówność jest spełniona, to $x_0$ jest poszukiwaną wartością pierwiastka. Zwracamy wynik i kończymy algorytm.
- W przeciwnym razie za nowy przedział poszukiwań pierwiastka przyjmujemy tą połówkę $[a,x_0]$ lub $[x_0,b]$, w której funkcja zmienia znak na krańcach.



Algorytm powtarzamy od początku dotąd, aż znajdziemy pierwiastek lub przedział $[a,b]$ osiągnie założoną długość (może to być również $\epsilon$ ). Wtedy kończymy zwracając ostatnio wyliczone $x_0$.

## 3. Implementacja

### Python

```python
def bisection(a, b, EPS_X, EPS_0):
    fa = f(a)
    fb = f(b)
    if fa == 0: return a
    if fb == 0: return b

    if fa * fb >= 0:
        print("Function doesn't meet requirements.")
        return

    mid = a
    while abs(b-a) > EPS_X:
        mid = (a + b) / 2

        if abs(f(mid)) < EPS_0:
            return mid

        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

    return (a+b)/2
```

### Java

```java
public static double bisection(double a, double b, double EPS_X, double EPS_0) {
        double fa = f(a);
        double fb = f(b);

        if (fa == 0) {
            return a;
        }
        if (fb == 0) {
            return b;
        }
        if (fa * fb >= 0) {
            System.out.println("Function doesn't meet requirements.");
            return Double.NaN;
        }

        double mid = a;

        while (Math.abs(b - a) > EPS_X) {
            mid = (a + b) / 2;

            if (Math.abs(f(mid)) < EPS_0) {
                return mid;
            }

            if (f(a) * f(mid) < 0) {
                b = mid;
            } else {
                a = mid;
            }
        }

        return (a + b) / 2;
    }
```

### C++

```cpp
double bisection(double a, double b, double EPS_X, double EPS_0) {
    double fa = f(a);
    double fb = f(b);

    if (fa == 0) {
        return a;
    }
    if (fb == 0) {
        return b;
    }
    if (fa * fb >= 0) {
        std::cout << "Function doesn't meet requirements." << std::endl;
        return NAN;
    }

    double mid = a;

    while (std::abs(b - a) > EPS_X) {
        mid = (a + b) / 2;

        if (std::abs(f(mid)) < EPS_0) {
            return mid;
        }

        if (f(a) * f(mid) < 0) {
            b = mid;
        } else {
            a = mid;
        }
    }

    return (a + b) / 2;
}

```
