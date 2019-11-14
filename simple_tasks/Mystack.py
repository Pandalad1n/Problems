class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        self.data.insert(0, x)

    def pop(self) -> None:
        self.data.pop(0)

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def getMin(self) -> int:
        return min(self.data)


obj = MinStack()
obj.push(5)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
