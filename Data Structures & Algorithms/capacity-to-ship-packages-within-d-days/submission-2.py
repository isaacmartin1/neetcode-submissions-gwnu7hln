class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
    
        def can_ship(capacity):
            ships = 1
            curr_cap = capacity
            for w in weights:
                if curr_cap - w < 0:
                    curr_cap = capacity
                    ships += 1
                curr_cap -= w
            return ships <= days
        
        while l <= r:
            m = (l + r) // 2
            if can_ship(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1


        return res

            