class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for i in range(1, len(strs)):
            curr = strs[i]
            if len(curr) == 0:
                return ""
            if len(curr) < len(res):
                res = res[:len(curr)]
            for curr_idx in range(len(curr)):
                if curr_idx >= len(res):
                    res = res[:curr_idx]
                    break
                if res[curr_idx] != curr[curr_idx]:
                    res = res[:curr_idx]
                    break
        
        return res