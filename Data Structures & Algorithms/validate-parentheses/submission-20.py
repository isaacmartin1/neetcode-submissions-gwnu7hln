class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        b = "({["
        e = "]})"
        bracket_dict = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for i in range(len(s)):
            print(brackets)
            if s[i] in b:
                brackets.append(s[i])
            else:
                if len(brackets) == 0:
                    return False

                if bracket_dict[s[i]] != brackets.pop():
                    return False
        
        if len(brackets) > 0:
            return False
        return True
