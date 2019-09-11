class Two_summ():
    def __init__(self, list, num):
        self.list = list
        self.num = num

    def multi_pass(self):
        for value in self.list:
            for second_value in self.list:
                print(value, "+", second_value, "=", value + second_value, "act", self.num)
                if value + second_value == self.num:
                    return True
        return False

    def multi_pass_unique(self):
        iter = 0
        for value in self.list:
            iter += 1
            for second_value in self.list[iter:]:
                print(value, "+", second_value, "=", value + second_value, "act", self.num)
                if value + second_value == self.num:
                    return True
        return False

    def single_pass(self):
        pass


print(Two_summ([4, 7, 1, -3, 2], 4).multi_pass_unique())
# True