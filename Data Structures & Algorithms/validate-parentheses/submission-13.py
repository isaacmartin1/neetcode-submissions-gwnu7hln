class Solution:
    def isValid(self, s: str) -> bool:
        front_side = []
        popped_values = 0
        for idx in range(len(s)):
            char = s[idx]
            if char == '[' or char == '{' or char == '(':
                front_side.insert(0, char)
            elif char == ']':
                if not front_side:
                    return False
                if front_side[0] == '[':
                    front_side.pop(0)
                else:
                    return False    
            elif char == '}':
                if not front_side:
                    return False
                if front_side[0] == '{':
                    front_side.pop(0)
                else:
                    return False    
            elif char == ')':
                if not front_side:
                    return False
                if front_side[0] == '(':
                    front_side.pop(0)
                else:
                    return False    

        return len(front_side) == 0
