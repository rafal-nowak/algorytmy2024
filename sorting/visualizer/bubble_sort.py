def bubbleSort(arr, highlites, *args):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            highlites[j] = 1
            highlites[j+1] = 1
            yield(2, 0)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield(2, 1)
            highlites[j] = 0
            highlites[j+1] = 2
    highlites[0] = 2
                