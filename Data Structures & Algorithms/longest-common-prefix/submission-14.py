class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        if len(strs) == 1:
            return res

        for s_idx in range(1, len(strs)):
            s = strs[s_idx]
            while not s.startswith(res):
                res = res[:-1]
                if res == "":
                    return res


        return res
