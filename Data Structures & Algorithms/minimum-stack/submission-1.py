class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        return self.stack.insert(0, val)

    def pop(self) -> None:
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        minimum = None
        print(self.stack)
        for idx in range(len(self.stack)):
            val = self.stack[idx]
            if minimum == None:
                minimum = val
            elif val < minimum:
                minimum = val
        return minimum
