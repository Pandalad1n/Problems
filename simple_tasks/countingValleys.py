def countingValleys(n, s):
    lvl = 0
    val_flag = False
    valleys = 0
    for i in s:
        if i == 'U':
            lvl += 1
        else:
            lvl -= 1

        if lvl < 0:
            val_flag = True
        elif val_flag:
            valleys += 1
            val_flag = False
    return valleys


print(countingValleys(8, 'UDDDUDUU'))
