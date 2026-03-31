class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = self.check_limit(nums, slow, 1)
            fast = self.check_limit(nums, fast, 2)

            if nums[slow] == nums[fast]:
                return nums[slow]        

    def check_limit(self, nums, index, increment):
        limit = len(nums) - 1
        while increment > 0:
            increment -= 1
            index += 1
            if index > limit:
                index = 0
        return index