class Non_dupe():
    def __init__(self, list):
        self.list = list

    def singleNumber(self):
        for num, value in enumerate(self.list):
            flag = False
            for second_num, second_value in enumerate(self.list):
                if value == second_value and num != second_num:
                    flag = True
            if not flag:
                return self.list[num]

    def singleNumber_O1(self):
        return False




# a = [1,2,3,54,5,6]
# a.pop(54)
# print(a)
print(Non_dupe([4, 3, 2, 4, 1, 3, 2, 5, 1]).singleNumber())
# 1