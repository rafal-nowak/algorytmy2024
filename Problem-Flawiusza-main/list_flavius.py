def flavius(n, k):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    while len(numbers) > 1:
        eliminated = (k - 1) % len(numbers)
        first = numbers[:eliminated]
        last = numbers[eliminated + 1:]
        numbers = last + first
    return numbers[0]