def leaders(arr):
    result = []
    n = len(arr)

    # przypisujemy zmiennej max wartość ostatniego elementu
    max = arr[-1]

    # ostatni element zawsze jest liderem
    result.append(max)

    # iterujemy po liście od prawej do lewej
    for i in range(n - 2, -1, -1):
        # jeśli wartość jest większa od maxa, to jest liderem
        if arr[i] > max:
            # aktualizujemy wartość zmiennej max
            max = arr[i]
            result.append(max)

    result.reverse()

    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(result)
