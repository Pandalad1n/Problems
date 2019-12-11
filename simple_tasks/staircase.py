
def staircase(n):
    stairs = ' ' * n
    for i in range(n):
        stairs = stairs[1:] + '#'
        print(stairs)

staircase(33)