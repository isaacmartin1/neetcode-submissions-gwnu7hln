class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        first_vals = nums[:-k]
        last_vals = nums[-k:]

        for idx in range(len(nums)):
            if idx < len(last_vals):
                nums[idx] = last_vals[idx]
            else:
                nums[idx] = first_vals[idx - len(last_vals)]


        # idx = 0
        # while idx < len(last_vals):
        #     nums[idx] = last_vals[idx]
        #     idx += 1

        # while idx < len(nums):
        #     nums[idx] = first_vals[idx - len(last_vals)]
        #     idx += 1

