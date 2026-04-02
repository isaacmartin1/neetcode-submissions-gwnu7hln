class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        
        for i in range(len(s)):
            start_i, end_i = i-1, i+1
            curr_str = s[i]

            if len(curr_str) > res_len:
                res =  curr_str
                res_len = len(curr_str)

            while start_i > -1 and end_i < len(s) and s[start_i] == s[end_i]:
                curr_str = s[start_i] + curr_str + s[end_i] 
                if len(curr_str) > res_len:
                    res = curr_str
                    res_len = len(curr_str)
                start_i -= 1
                end_i += 1
            
            start_i, end_i = i, i + 1
            curr_str = ""            
            while start_i > -1 and end_i < len(s) and s[start_i] == s[end_i]:
                curr_str = s[start_i] + curr_str + s[end_i]
                if len(curr_str) > res_len:
                    res = curr_str
                    res_len = len(curr_str)
                start_i -= 1
                end_i += 1
        
        return res
