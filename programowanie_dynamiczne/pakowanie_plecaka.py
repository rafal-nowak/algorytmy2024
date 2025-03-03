def knapsack(W, items):
    # etap 1 - programowanie dynamiczne
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(W + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])
            else:
                dp[i][w] = dp[i - 1][w]

    # etap 2 - rekonstrukcja odpowiedzi
    w = W
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]

    return dp[n][W], selected_items[::-1]


capacity = int(input("Podaj pojemność plecaka: "))
count = int(input("Podaj liczbę przedmiotów: "))
items = []
for i in range(count):
    value, weight = list(map(int, input(f"Podaj parametry przedmiotu nr {i+1} (wartość, waga): ").split()))
    items.append((value, weight))

value_sum, chosen_items = knapsack(capacity, items)

print(f"Maksymalna suma wartości przedmiotów w plecaku: {value_sum}")
print("Wybrane przedmioty:")
for value, weight in chosen_items:
    print(f"\t({value} {weight})")