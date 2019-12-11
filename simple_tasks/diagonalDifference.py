def diagonalDifference(arr):
    i = dia1 = dia2 = 0
    j = len(arr) - 1
    for row in arr:
        dia1 += row[i]
        dia2 += row[j]
        i += 1
        j -= 1
    return abs(dia1 - dia2)

print(diagonalDifference([[11, 2, 4],
                          [4, 5, 6],
                          [10, 8, -12]]))
