class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase = prices[0]
        res = 0


        if len(prices) == 1:
            return res

        for p_idx in range(1, len(prices)):
            p = prices[p_idx]
            prev_p = prices[p_idx - 1]
            # print('prev p', prev_p, 'curr p', p, 'purchase price', purchase)
            if p < prev_p and prev_p > purchase:
                print('happen 1')
                res += prev_p - purchase
                purchase = p
            elif p < purchase:
                purchase = p
            elif p_idx == len(prices) - 1 and p > purchase:
                print('happen 2')
                res += p - purchase
        
        return res

            
