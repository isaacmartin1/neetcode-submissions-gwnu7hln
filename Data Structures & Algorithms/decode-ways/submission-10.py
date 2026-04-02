class Solution:
    def numDecodings(self, s: str) -> int:
        count_dict = { len(s) : 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                count_dict[i] = 0
            else:
                count_dict[i] = count_dict[i + 1]

            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                count_dict[i] += count_dict[i + 2]
        

        return count_dict[0]