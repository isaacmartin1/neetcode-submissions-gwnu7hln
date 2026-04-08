class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x > 10 * div:
            div *= 10
        
        while div >= 1:
            r = x % 10
            l = x // div

            if l != r: return False

            x = (x % div) // 10
            div //= 100
        
        return True