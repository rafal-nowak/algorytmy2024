def fibonacci(n):
    if n <= 0:
        print("N musi być większe od 0")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = int(input("Podaj wartość n: "))
    print(f"{n}-ty element ciągu Fibonacciego to: {fibonacci(n)}")