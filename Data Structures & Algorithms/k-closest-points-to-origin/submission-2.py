import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p
            dist_to_origin = -(x ** 2 + y ** 2)** .5
            heapq.heappush(heap, (dist_to_origin, p))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        while heap:
            _, p= heapq.heappop(heap)
            res.append(p)
        return res