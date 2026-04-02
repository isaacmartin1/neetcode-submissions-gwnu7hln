class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            l, r = i, i
            res, res_len = self.helper(l, r, s, res, res_len)

            l, r = i, i + 1
            res, res_len = self.helper(l, r, s, res, res_len)
        return res

    def helper(self, l, r, s, res, res_len):
        while l > -1 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res_len = r - l + 1
                res = s[l: r + 1]
            l -= 1
            r += 1
        return res, res_len