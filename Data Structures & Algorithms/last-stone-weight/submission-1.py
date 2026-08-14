import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        print(heap)
        
        while heap and len(heap) > 1:
            print(heap)
            larger = heapq.heappop(heap)
            smaller = heapq.heappop(heap)


            if larger != smaller:
                heapq.heappush(heap, larger - smaller)
        print(heap)
        return 0 if not heap else heap[0] * -1