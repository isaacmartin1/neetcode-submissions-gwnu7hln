class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prev = prices[0]
        for i in range(1, len(prices)):
            prev = prices[i - 1]
            curr = prices[i]
            if curr > prev:
                res += curr - prev

        return res
