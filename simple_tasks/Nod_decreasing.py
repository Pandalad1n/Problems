from copy import copy

class Not_decreasing():
    def __init__(self, list):
        self.list = list

    def check(self):
        for iter in range(len(self.list)):
            counter = 0
            temp_list = copy(self.list)
            temp_list.pop(iter)
            for sec_iter in range(len(temp_list) - 1):
                if temp_list[sec_iter] <= temp_list[sec_iter + 1]:
                    counter += 1
            if counter == len(temp_list) - 1:
                return True
        return False

    def check_On(self):
        counter = 0
        for iter in range(len(self.list) - 1):
            if self.list[iter] > self.list[iter + 1]:
                counter += 1
            if counter >= 2:
                return False
        return True


print(Not_decreasing([3, 2, 1]).check_On())
# True
print(Not_decreasing([5, 1, 3, 2, 5]).check_On())
# False
