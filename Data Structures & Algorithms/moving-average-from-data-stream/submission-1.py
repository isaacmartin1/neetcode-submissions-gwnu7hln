class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = collections.deque()
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.total -= self.window.popleft()
        
        self.window.append(val)
        self.total += val

        return self.total / len(self.window)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
