# Funkcja pomocnicza do określenia priorytetu operatorów
def get_precedence(op):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence.get(op, 0)


# Funkcja pomocnicza do sprawdzenia, czy dany znak jest operatorem
def is_operator(token):
    return token in {'+', '-', '*', '/', '^'}


# Algorytm Shunting Yard do konwersji infiksowego wyrażenia na ONP
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

    # Przenieś pozostałe elementy ze stosu do wyjścia
    while stack:
        output.append(stack.pop())

    return output


# Kalkulator ONP do obliczenia wyniku wyrażenia w ONP
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


# Funkcja końcowa, która przyjmuje wyrażenie infiksowe jako string i zwraca wynik
def calculate(expression):
    rpn_expression = infix_to_rpn(expression)
    result = evaluate_rpn(rpn_expression)
    return result

if __name__ == '__main__':
    # Przykład użycia
    expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
    print("Wyrażenie infiksowe:", expression)
    rpn_expression = infix_to_rpn(expression)
    print("Wyrażenie ONP:", " ".join(rpn_expression))
    result = calculate(expression)
    print("Wynik:", result)
