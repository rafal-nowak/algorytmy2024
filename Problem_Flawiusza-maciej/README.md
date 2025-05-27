# Problem Józefa Flawiusza

## 1. Czym jest problem Flawiusza?

Jest to problem teoretyczny z zakresu kombinatoryki. W ogólnej wersji problem brzmi następująco: na okręgu ustawiamy n obiektów, następnie eliminujemy co k-ty obiekt, tak długo, aż zostanie tylko jeden.
1. Wyobraź sobie grupę n osób stojących w kole.
2. Zaczynamy od pierwszej osoby, a następnie eliminujemy co k-tą osobę (licząc od aktualnej pozycji).
3. Proces powtarzamy, aż pozostanie tylko jedna osoba.
4. Pytanie brzmi: Który osoba pozostanie jako ostatnia?
---

---
## 2. Implementacja w Pythonie
```python
def flawiusz(n):
    people = list(range(1, n + 1))
    index = 0

    while len(people) > 1:
        index = (index + 1) % len(people)  
        people.pop(index)

    return people[0]


n = int(input("Podaj liczbę osób"))  
print("Ostatnia osoba to osoba:", flawiusz(n))
```
## 3. Przykład dla k = 2

![Bez nazwy](https://github.com/user-attachments/assets/f298d069-00e8-4f1a-a757-58672eab0e9d)
## Jakie zależności tu widzimy?
- liczby parzyste zawsze są eliminowane pierwsze
- dla każdej potęgi 2 zawsze zostaje 1 osoba
- Im bilżej kolejnej potęgi 2 numer ostatniej osoby systematycznie zwiększa się o 2
---
## 4. Wykorzystanie 
- Problem ten możemy wykorzystać chcąc zaszyfrować wiadomość
- Przykład, co druga litera: FLAWIUSZ ⭢ LWUZASIF
- Przykład, co trzecia litera: PROBLEM ⭢ OERMLPB
```python
def flawiusz(text, step):
    result = ""
    idx = 0
    while text:
        idx = (idx + step - 1) % len(text)
        result += text[idx]
        text = text[:idx] + text[idx + 1:]
    return result


text = input("Podaj wyraz: ")
step = int(input("Podaj liczbę: "))
print("\nWynik:", flawiusz(text, step))
```
## 5. Podsumowanie
- Problem Flawiusza to ciekawy temat i można go rozpatrywać a także wykorzystywać na różne sposoby
- Jeśli temat cię zaciekawił tu możesz przeczytać więcęj ⭢ https://home.agh.edu.pl/~zobmat/2021/pedzich_maciej/#/
