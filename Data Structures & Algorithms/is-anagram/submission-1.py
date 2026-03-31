class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        
        for s_letter in s:
            if s_letter not in s_dict:
                s_dict[s_letter] = 1
            else:
                s_dict[s_letter] += 1
        
        for t_letter in t:
            if t_letter in s_dict:
                s_dict[t_letter] -= 1
            else:
                return False

        for value in s_dict.values():
            print(value)
            if value != 0:
                return False
        return True