class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        b = "({["
        bracket_dict = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for char in s:
            if char in b:
                brackets.append(char)
            else:
                if len(brackets) == 0:
                    return False
                if bracket_dict[char] != brackets.pop():
                    return False
        
        if len(brackets) > 0:
            return False

        return True
