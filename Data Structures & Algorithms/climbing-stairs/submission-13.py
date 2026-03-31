class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        val = n
        

        while val >= 0:
            subtotal = 0
            if cache.get(val + 1):
                subtotal += cache[val + 1]
            
            if cache.get(val + 2):
                subtotal += cache[val + 2]
            
            if not cache.get(val + 1) and not cache.get(val + 2):
                subtotal = 1

            cache[val] = subtotal
        

            val -= 1
        print(cache)
        return cache[0]