def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid

    return right
