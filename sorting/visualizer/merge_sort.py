def merge(arr, left, mid, right, highlites):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:left+n1]
    R = arr[left+n1:mid+n2+1]

    i = 0  
    j = 0  
    k = left

    while i < n1 and j < n2:
        highlites[left+i] = 1
        highlites[left+n1+j] = 1
        yield(2, 3)
        highlites[left+i] = 2
        highlites[left+n1+j] = 2
        if L[i] <= R[j]:
            i += 1
        else:
            j += 1
        k += 1

    while i < n1:
        highlites[left+i] = 1
        yield(1, 1)
        highlites[left+i] = 2
        i += 1
        k += 1

    while j < n2:
        highlites[left+n1+j] = 1
        yield(1, 1)
        highlites[left+n1+j] = 2
        j += 1
        k += 1

    i = 0  
    j = 0  
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        highlites[k] = 2
        yield(1, 0)
        k += 1

    while i < n1:
        arr[k] = L[i]
        highlites[k] = 2
        yield(1, 0)
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        highlites[k] = 2
        yield(1, 0)
        j += 1
        k += 1


def mergeSort(arr, highlites, left, right):
    if right-left>1:
        mid = (left + right) // 2

        highlites[left] = 1
        highlites[right] = 1

        yield(0, 1)

        highlites[right] = 0

        sort = mergeSort(arr, highlites, left, mid)
        step = next(sort, None)
        while step is not None:
            yield(step[0], step[1])
            step = next(sort, None)

        sort = mergeSort(arr, highlites, mid + 1, right)
        step = next(sort, None)
        while step is not None:
            yield(step[0], step[1])
            step = next(sort, None)

        merge_step = merge(arr, left, mid, right, highlites)
        step = next(merge_step, None)
        while step is not None:
            yield(step[0], step[1])
            step = next(merge_step, None)
    elif arr[left]>arr[right]:
        highlites[left] = 1
        highlites[right] = 1
        yield(2, 1)

        arr[left], arr[right] = arr[right], arr[left]

        highlites[left] = 2
        highlites[right] = 2
        yield(2, 0)
    else:
        highlites[left] = 1
        highlites[right] = 1
        yield(0, 0)
        highlites[left] = 2
        highlites[right] = 2
        yield(0, 0)
