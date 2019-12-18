def rotLeft(a, d):
    for i in range(d):
        for j in range(len(a) - 1):
            a[j], a[j + 1] = a[j + 1], a[j]
    return a


print(rotLeft([1, 2, 3, 4], 1))
