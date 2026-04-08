class Solution:
    def isPalindrome(self, x: int) -> bool:
        conv = str(x)

        if len(conv) % 2 == 0: # even
            l = int((len(conv) - 1) // 2)
            r = l + 1
        else: # odd
            l = r = int((len(conv) - 1) / 2) 

        while l >= 0 and r < len(conv):
            if conv[l] != conv[r]:
                return False
            l -= 1
            r += 1
        return True