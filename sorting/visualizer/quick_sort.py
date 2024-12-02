def quickSort(arr, highlites, low, high):
    if (low < high):

        pivot = arr[low]
        highlites[low] = 3
        yield(1, 1)
        i = low
        j = high
        highlites[i] = 1
        highlites[j] = 1
        yield(0, 0)

        while (True):
            while (arr[i] < pivot):
                highlites[i] = 0
                i += 1
                highlites[i] = 1
                yield(1, 1)
            yield(1, 1)

            while (arr[j] > pivot):
                highlites[j] = 0
                j -= 1
                highlites[j] = 1
                yield(1, 1)
            yield(1, 1)

            if (i >= j):
                highlites[i] = 2
                yield(0, 1)
                break

            arr[i], arr[j] = arr[j], arr[i]
            yield(2, 0)


        sort = quickSort(arr, highlites, low, i - 1)
        step = next(sort, None)
        while step is not None:
            yield(step[0], step[1])
            step = next(sort, None)
        sort = quickSort(arr, highlites, i + 1, high)
        step = next(sort, None)
        while step is not None:
            yield(step[0], step[1])
            step = next(sort, None)
    
    if low != len(arr): highlites[low] = 2
    yield(0, 1)
