class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.heap.sort()
        while len(self.heap) > self.k:
            self.heap.pop(0)
        return self.heap[0]
