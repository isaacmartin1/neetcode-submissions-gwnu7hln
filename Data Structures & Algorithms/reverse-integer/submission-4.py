class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1

        is_neg = x < 0
        x = abs(x)

        res = 0

        while x:
            digit = x % 10
            x //= 10

            if res > MAX // 10 or (res == MAX // 10 and MAX % 10 < digit):
                return 0
            
            res = res * 10 + digit
        
        return -res if is_neg else res