import math
class MinStack:
    '''
    Alternaive solution:
        use another stack to record current minimum value
    '''
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack != []:
            return self.stack[len(self.stack)-1]
        else:
            return []

    def getMin(self) -> int:
        if self.stack != []:
            min = math.inf
            for i in self.stack:
                if i < min:
                    min = i
            return min
        else:
            return []

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    sol = MinStack()
    sol.push(3)
    sol.push(2)
    sol.push(1)
    sol.pop()
    print(sol.top())
    print(sol.getMin())

