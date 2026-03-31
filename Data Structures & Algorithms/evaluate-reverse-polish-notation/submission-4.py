class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operators = "+-*/"
        for t in tokens:
            if t in operators:
                print('111111111111111111111111')
                print(numbers)
                second_num = numbers.pop(-1)
                first_num = numbers.pop(-1)
                if t == '+':
                    first_num += second_num
                elif t == '-':
                    first_num -= second_num
                elif t == '*':
                    first_num *= second_num
                elif t == '/':
                    first_num = int(first_num / second_num)
                numbers.append(first_num)               
            else:
                numbers.append(int(t))
        
        return numbers[0]