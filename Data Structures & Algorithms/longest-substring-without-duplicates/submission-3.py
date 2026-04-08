class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        curr_set = set()

        for i in range(len(s)):
            if s[i] in curr_set:
                while s[i] in curr_set:
                    curr_set.remove(s[l])
                    l += 1
                curr_set.add(s[i])
            
            else:
                curr_set.add(s[i])
                res = max(res, len(curr_set))
        
        return res