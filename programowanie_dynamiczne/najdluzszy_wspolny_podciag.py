def find_lcs(a, b):
    # etap 1 - programowanie dynamiczne
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for ai in range(1, len(a) + 1):
        for bi in range(1, len(b) + 1):
            if a[ai - 1] == b[bi - 1]:
                dp[ai][bi] = dp[ai - 1][bi - 1] + 1
            else:
                dp[ai][bi] = max(dp[ai - 1][bi], dp[ai][bi - 1])

    # etap 2 - rekonstrukcja odpowiedzi
    cur_ai = len(a)
    cur_bi = len(b)
    letters = []
    while cur_ai > 0 and cur_bi > 0:
        if a[cur_ai - 1] == b[cur_bi - 1]:
            letters.append(a[cur_ai - 1])
            cur_ai -= 1
            cur_bi -= 1
        elif dp[cur_ai - 1][cur_bi] > dp[cur_ai][cur_bi - 1]:
            cur_ai -= 1
        else:
            cur_bi -= 1

    return "".join(letters[::-1])


if __name__ == "__main__":
    word_1, word_2 = input("Podaj 2 słowa, dla których ma być znaleziony najdłuższy wspólny podciąg: ").split()
    lcs = find_lcs(word_1, word_2)

    print(f"Najdłuższy wspólny podciąg to: {lcs}")
