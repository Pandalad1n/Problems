class Solution1:
    def getRange(self, arr, target):
        first_occur = -1
        last_occur = -1
        for iter in range(len(arr)):
            if arr[iter] == target:
                if first_occur == -1:
                    first_occur = iter
                last_occur = iter
        return first_occur, last_occur


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution1().getRange(arr, x))
# [1, 4]
