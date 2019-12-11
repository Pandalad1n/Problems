def jumpingOnClouds(c):
    pos = 0
    jumps = 0
    while pos < len(c) - 2:
        if c[pos+2] != 1:
            pos += 2
            jumps += 1
        else:
            jumps += 1
            pos += 1

    if pos != len(c) - 1:
        return jumps + 1
    return jumps


print(jumpingOnClouds([0, 0, 0, 0, 1, 0, 0]))
