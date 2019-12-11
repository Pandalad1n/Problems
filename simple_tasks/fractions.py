
def plusMinus(arr):
    pos = neg = zeros = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zeros += 1

    print(round(pos / len(arr), 6))
    print(round(neg / len(arr), 6))
    print(round(zeros / len(arr), 6))
    print(round(1 / 6, 6))


plusMinus([-4, 3, -9, 0, 4, 1])