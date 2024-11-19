import math

def is_range_correct(n):
    return True if n > 2 and n%1==0 else False

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)  # Tworzymy liste z wszystkimi wartościami True

    # 0 i 1 nie sa liczbami pierwszymi
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return is_prime

def find_prime_numbers(n):
    is_prime = sieve_of_eratosthenes(n)

    # Tworzymy liste z samymi liczbami pierwszymi z podanego przedzialu
    prime_numbers = []

    for x in range(2, n + 1):
        if is_prime[x] == True:
            prime_numbers.append(x)

    return prime_numbers

def print_prime_numbers(n):
    is_prime = sieve_of_eratosthenes(n)

    for x in range(2, n+1):
        if is_prime[x] == True:
            print(x)

def prime_factorization(n):
    prime_numbers = find_prime_numbers(n)
    prime_factors = []

    while n != 1:
        x = 0
        while n%prime_numbers[x] != 0:
            x += 1
        prime_factors.append(prime_numbers[x])
        n /= prime_numbers[x]

    return prime_factors


if __name__ == '__main__':
    print("   ---   Sito Eratostenesa  ---   \n")

    n = int(input("Podaj n: "))

    if is_range_correct(n) == False:
        print("Podano nieprawidlowy przedzial!")
        quit()

    print(prime_factorization(n))
