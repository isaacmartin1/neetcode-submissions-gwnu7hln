class Solution:
    def reverse(self, x: int) -> int:
        minimum = (-2)**31
        maximum = 2**31-1

        res = 0

        is_neg = x < 0
        x = abs(x)

        while x:
            next_digit = x % 10
            x //= 10
            if res == 0:
                res = next_digit
            else:
                proposed_num = res / maximum
                if proposed_num * 10 > 1:
                    return 0

                res *= 10
                res += next_digit

        if is_neg:
            return res * -1

        return res