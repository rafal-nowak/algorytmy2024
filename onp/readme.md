# Wprowadzenie do Odwrotnej Notacji Polskiej (ONP)

## 1. Czym jest Odwrotna Notacja Polska?
Odwrotna Notacja Polska (ONP), znana również jako Notacja Postfiksowa, to sposób zapisu wyrażeń matematycznych, w którym operatory występują po operandach. 

### Zalety ONP:
- **Brak potrzeby użycia nawiasów** – dzięki jednoznacznemu zapisu kolejność działań jest zawsze jasna.
- **Łatwość implementacji** – ONP jest łatwiejsza do implementacji w programach komputerowych, ponieważ eliminuje potrzebę skomplikowanej analizy wyrażeń infiksowych.

### Przykłady:
1. Wyrażenie infiksowe `3 + 4` w ONP zapisujemy jako `3 4 +`.
2. Wyrażenie infiksowe `5 + (2 * 3)` w ONP to `5 2 3 * +`.

---

## 2. Stos i zasada działania ONP
ONP korzysta ze stosu do obliczania wyrażeń.

### Zasady działania:
1. **Przechodzimy od lewej do prawej** przez wyrażenie w ONP.
2. Jeśli napotkamy **liczbę**, umieszczamy ją na stosie.
3. Jeśli napotkamy **operator**, zdejmujemy dwie liczby ze stosu, wykonujemy operację i wynik umieszczamy na stosie.
4. Po przejściu całego wyrażenia, na stosie powinna pozostać jedna liczba – wynik wyrażenia.

### Przykład obliczania ONP `3 4 + 2 *`:
- **Stos początkowy**: []
- **Czytamy `3`**: [3]
- **Czytamy `4`**: [3, 4]
- **Czytamy `+`**: 3 + 4 = 7 → [7]
- **Czytamy `2`**: [7, 2]
- **Czytamy `*`**: 7 * 2 = 14 → [14]
- **Wynik**: 14

---

## 3. Algorytm Shunting Yard do konwersji infiksowego wyrażenia na ONP

Algorytm Shunting Yard autorstwa Edsgera Dijkstry służy do konwersji wyrażeń infiksowych na ONP. Obsługuje kolejność działań oraz nawiasy.

### Kroki algorytmu:
1. Zainicjuj pustą listę `output` i pusty `stack`.
2. Dla każdego elementu wyrażenia (tzw. tokenu):
   - **Jeśli token to liczba** – dodaj go do `output`.
   - **Jeśli token to operator**:
     - Dopóki operator na szczycie stosu ma wyższy lub równy priorytet niż bieżący operator, przenieś operator ze stosu do `output`.
     - Dodaj bieżący operator na stos.
   - **Jeśli token to lewy nawias `(`** – dodaj go na stos.
   - **Jeśli token to prawy nawias `)`** – przenieś operatory ze stosu do `output` aż do napotkania lewego nawiasu, który usuwamy.
3. Przenieś wszystkie pozostałe operatory ze stosu do `output`.

### Priorytety operatorów:
- `+`, `-` mają najniższy priorytet (1)
- `*`, `/` mają wyższy priorytet (2)
- `^` (potęgowanie) ma najwyższy priorytet (3)

---

## 4. Implementacja kalkulatora ONP w Pythonie

Poniżej znajduje się kod w Pythonie, który realizuje konwersję wyrażenia infiksowego do ONP oraz oblicza wynik wyrażenia w ONP.

### Funkcja `infix_to_rpn` - konwersja infiksowego wyrażenia na ONP:

```python
def get_precedence(op):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence.get(op, 0)

def is_operator(token):
    return token in {'+', '-', '*', '/', '^'}

def infix_to_rpn(expression):
    output = []
    stack = []
    tokens = expression.replace("(", " ( ").replace(")", " ) ").split()  # Tokenizacja
    
    for token in tokens:
        if token.isdigit() or token.replace('.', '', 1).isdigit():  # Liczba
            output.append(token)
        elif token == '(':  # Lewy nawias
            stack.append(token)
        elif token == ')':  # Prawy nawias
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Usunięcie lewego nawiasu ze stosu
        elif is_operator(token):  # Operator
            while (stack and stack[-1] != '(' and
                   get_precedence(stack[-1]) >= get_precedence(token)):
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return output
```

### Funkcja `evaluate_rpn` - obliczanie wyrażenia ONP:

```python
def evaluate_rpn(rpn_expression):
    stack = []
    
    for token in rpn_expression:
        if token.replace('.', '', 1).isdigit():  # Liczba
            stack.append(float(token))
        elif is_operator(token):  # Operator
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b if b != 0 else float('inf'))  # Unikaj dzielenia przez zero
            elif token == '^':
                stack.append(a ** b)
    
    return stack[0] if stack else None  # Wynik końcowy
```

### Funkcja `calculate` - łączenie obu funkcji:

```python
def calculate(expression):
    rpn_expression = infix_to_rpn(expression)
    result = evaluate_rpn(rpn_expression)
    return result
```

### Przykład użycia:

```python
expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
print("Wyrażenie infiksowe:", expression)
rpn_expression = infix_to_rpn(expression)
print("Wyrażenie ONP:", " ".join(rpn_expression))
result = calculate(expression)
print("Wynik:", result)
```

### Przykład wyników:
```
Dla wyrażenia:

Wyrażenie infiksowe: 3 + 4 * 2 / ( 1 - 5 ) ^ 2
Wyrażenie ONP: 3 4 2 * 1 5 - 2 ^ / +
Wynik: 3.5
```


## 5. Zadania
1. Przekształć następujące wyrażenia infiksowe na ONP:
- 5 + 2 * (3 - 1)
- (7 - 2) ^ 2 / 4 + 6
2. Napisz funkcję do obsługi dodatkowych funkcji matematycznych w wyrażeniach ONP, takich jak sin, cos, sqrt.
3. Rozbuduj kalkulator o walidację danych wejściowych oraz obsługę wyjątków.

## Dodatkowe materiały
- Wikipedia - Odwrotna Notacja Polska https://pl.wikipedia.org/wiki/Odwrotna_notacja_polska
- Wikipedia - Edsger Dijkstra i algorytm Shunting Yard https://en.wikipedia.org/wiki/Shunting-yard_algorithm