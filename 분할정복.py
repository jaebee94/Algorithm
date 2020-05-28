def recursive_power(C, n):
    if n == 1:
        return C
    if n % 2 == 0:
        y = recursive_power(C, n/2)
        return y * y
    else:
        y = recursive_power(C, n/2)
        return y * y * C

