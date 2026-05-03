import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            k = (left + right) // 2

            hours_used = 0

            for pile in piles:
                hours_used += math.ceil(pile / k)
            
            if hours_used > h:
                left = k + 1

            else: 
                right = k
                
        return left