class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res_count = 0

        for i in range(len(s)):
            l, r = i, i
            self.helper(l, r, s)

            l, r = i, i + 1
            self.helper(l, r, s)
    
        return self.res_count

    def helper(self, l, r, s):
        while l > -1 and r < len(s) and s[l] == s[r]:
            self.res_count += 1
            l -= 1
            r += 1