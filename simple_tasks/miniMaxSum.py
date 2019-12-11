
def miniMaxSum(arr):
    arr.sort()
    print( sum(arr[:len(arr) - 1]), sum(arr[1:]))


miniMaxSum([1,2,3,4,5])
