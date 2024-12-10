def floorSqrt(n):
    if n == 0 or n == 1:
        return n

    left = 1
    right = n
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid

        if mid * mid < n:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

if __name__ == "__main__":
    print(floorSqrt(63))


