def evaluate_rpn(expression):
    stack = []
    for token in expression:
        if token.isdigit():  # Jeśli token jest liczbą
            stack.append(int(token))
        else:  # Token to operator
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            stack.append(result)
    return stack[0]  # Wynik znajduje się na wierzchu stosu

if __name__ == '__main__':
    expression = ["3", "4", "+", "2", "*"]
    result = evaluate_rpn(["3", "4", "+", "2", "*"])
    print(f"expression: {expression}")
    print(f"result: {result}")
