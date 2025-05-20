def fibonacci(n):
    if n <= 0:
        print("N musi być większe od 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a = 0
    b = 1
    for _ in range(2, n):
        temp = a + b
        a = b
        b = temp
    return b
    
if __name__ == "__main__":
    n = int(input("Podaj wartość n: "))
    print(f"{n}-ty element ciągu Fibonacciego to: {fibonacci(n)}")