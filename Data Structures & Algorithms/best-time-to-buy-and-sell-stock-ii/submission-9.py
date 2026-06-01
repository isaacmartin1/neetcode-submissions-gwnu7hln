class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(1, len(prices)):
            curr = prices[i]
            prev = prices[i - 1]
            
            if curr > prev:
                res += curr - prev
            
        return res
