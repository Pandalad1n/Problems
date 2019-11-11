def fibb(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, b+a


fibb(100)

'0, 1 , 1 , 2 , 3, 5'
