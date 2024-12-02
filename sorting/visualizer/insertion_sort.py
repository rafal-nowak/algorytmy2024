def insertionSort(arr, highlites, *args):
 
    for i in range(len(arr)):
        j = i
        while j != 0 and arr[j] < arr[j-1]:
            highlites[j] = 1
            highlites[j-1] = 3
            yield(2, 1)
            arr[j], arr[j-1] = arr[j-1], arr[j]
            highlites[j] = 2
            highlites[j-1] = 2
            j -= 1
        highlites[j] = 1
        if j != 0: highlites[j-1] = 3
        yield(2, 0)
        highlites[j] = 2
        if j != 0: highlites[j-1] = 2