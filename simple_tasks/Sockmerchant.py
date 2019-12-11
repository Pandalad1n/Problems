def sockMerchant(n, ar):
    pairs = 0
    for num in set(ar):
        pairs += ar.count(num) // 2
    return pairs


print(sockMerchant(10, [1, 1, 3, 4, 5, 6, 7, 8, 9, 10]))
