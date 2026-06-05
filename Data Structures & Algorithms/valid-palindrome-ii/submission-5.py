class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        mulligan = False

        while left <= right:
            if s[right] != s[left]:
                # if mulligan:
                #     return False

                # mulligan = True
                if is_palindrome(left, right - 1) or is_palindrome(left + 1, right):
                    return True
                else:
                    return False
                
            
            left += 1
            right -= 1

        return True
