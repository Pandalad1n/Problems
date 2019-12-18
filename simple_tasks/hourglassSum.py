
def hourglassSum(arr):
    max_hg = -10
    x = 0
    y = 0
    while x < 4 and y < 4:
        hg = \
            arr[y][x] + arr[y][x+1] + arr[y][x+2] + \
            arr[y+1][x+1] + \
            arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
        max_hg = max(max_hg, hg)
        if x > 2:
            y += 1
            x = 0
            continue
        x += 1
    return max_hg


print(hourglassSum([
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
))
