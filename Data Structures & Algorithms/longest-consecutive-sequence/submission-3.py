class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        res = 0

        for number in set_of_nums:
            if (number + 1) not in set_of_nums:
                streak = 1
                while (number - streak) in set_of_nums:
                    streak += 1
                res = max(streak, res)

        return res
