class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        consec_nums = {}
        res = 1
        # sort array
        nums.sort()
        # do evaluation
        for n in nums:
            if n - 1 in consec_nums.keys():
                val = consec_nums[n - 1] + 1
                consec_nums[n] = val
                res = max(res, val)
            else:
                consec_nums[n] = 1
            
            
        return res