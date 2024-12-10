def binary_search_iterative(arr, left, right, x):

    # Warunek dla zakończenia szukania wartości
    while left <= right:

        # Wyznaczamy środek rozpatrywanego zbioru danych
        mid = (right + left) // 2

        # Sprawdzamy, czy szukana wartość znajduje się w środku
        if arr[mid] == x:
            return mid

        # Jeśli szukana wartość jest większa, ignorujemy lewą stronę
        elif arr[mid] < x:
            left = mid + 1

        # Jeśli szukana wartość jest mniejsza, ignorujemy prawą stronę
        else:
            right = mid - 1

    # Jeśli dojdziemy tutaj, oznacza to, że wartość nie występuje w zbiorze danych
    return -1

def binary_search_recursive(arr, left, right, x):

    if right >= left:
        mid = (right + left) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search_recursive(arr, left, mid - 1, x)

        else:
            return binary_search_recursive(arr, mid + 1, right, x)

    else:
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 4

    result = binary_search_recursive(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")


