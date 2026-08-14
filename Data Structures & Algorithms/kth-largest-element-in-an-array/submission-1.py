import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapq.heapify(h)
        res = 0
        while k > 0:
            res = heapq.heappop(h)
            k -= 1
        
        return -res