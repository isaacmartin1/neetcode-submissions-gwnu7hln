class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for idx in range(len(nums)):
            specific_result = 1

            current_nums = nums[0:idx]

            for n in nums[idx+1:]:
                current_nums.append(n)
            
            for n in current_nums:
                specific_result *= n


            output.append(specific_result)
        
        return output

