class MyStack:

    def __init__(self):
        self.frame = []

    def push(self, x: int) -> None:
        self.frame.append(x)

    def pop(self) -> int:
        
        var = self.frame.pop(-1)
        return var

    def top(self) -> int:

        var = self.frame[-1]
        return var

    def empty(self) -> bool:
        if self.frame:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()