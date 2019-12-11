def repeatedString(s, n):
    fit = n // len(s)
    tail = n % len(s)
    return s.count('a') * fit + s[:tail].count('a')


print(repeatedString('asa', 10))
