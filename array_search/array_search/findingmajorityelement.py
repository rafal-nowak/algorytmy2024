def majority_element(arr):
    result = 0
    count = 0

    for i in arr:
        if count == 0:
            result = i
        count += (1 if i == result else -1)

    count = 0

    for i in arr:
        count += 1 if i == result else 0

    return result if count > len(arr)//2 else -1


if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    print(majority_element(arr))