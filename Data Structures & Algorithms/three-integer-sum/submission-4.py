class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1 # left side just to right of the a, and right always starts at last element

            while l < r:
                proposal = a + nums[l] + nums[r]

                if proposal > 0:
                    r -= 1
                elif proposal < 0:
                    l += 1
                elif proposal == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res