class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.res_len = 0

        for i in range(len(s)):
            l, r = i, i
            self.helper(l, r, s)

            l, r = i, i + 1
            self.helper(l, r, s)
        return self.res

    def helper(self, l, r, s):
        while l > -1 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > self.res_len:
                self.res_len = r - l + 1
                self.res = s[l: r + 1]
            l -= 1
            r += 1
