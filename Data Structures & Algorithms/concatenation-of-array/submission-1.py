class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        i = 0

        while i < 2:
            for n in nums:
                res.append(n)

            i += 1

        return res