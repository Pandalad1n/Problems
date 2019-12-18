def minimumBribes(q):
    shifts = 0
    q = [val - 1 for val in q]
    for i, val in enumerate(q):
        if val - i > 2:
            print("Too chaotic")
            return
        for j in range(max(val - 1, 0), i):
            if q[j] > val:
                shifts += 1
    print(shifts)


minimumBribes([1, 2, 5, 6, 7, 3, 4])
# minimumBres([0, 1, 2, 3, 4, 5, 6])
