class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))



    def helper(self, nums):
        print(nums)
        prev, curr = 0, 0

        for n in nums:
            tmp = curr
            curr = max(n + prev, curr)
            prev = tmp
        return curr
