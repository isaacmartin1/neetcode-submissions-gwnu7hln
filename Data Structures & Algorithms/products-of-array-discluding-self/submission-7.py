class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        prefix = []
        suffix = []

        # establish pre-fix
        prefix_val = 1

        for idx in range(len(nums)):
            if idx != 0:
                prefix_val *= nums[idx-1]

            prefix.append(prefix_val)

        # establish suffix
        suffix_val = 1
        for idx in range(len(nums)-1, -1, -1):
            print(idx)
            if idx != len(nums) - 1:
                suffix_val *= nums[idx+1]
            # add to beginning of list
            suffix.insert(0, suffix_val)

        # populate output
        for idx in range(len(output)):
            output[idx] = suffix[idx] * prefix[idx]
        
        return output
