class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r != len(prices):
            pft = prices[r] - prices[l]
            if pft >= 0:
                res = max(res, pft)
            else:
                l = r
            r += 1

        return res