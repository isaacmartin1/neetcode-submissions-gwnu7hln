class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        





        def helper(numbers):
            rob1, rob2 = 0, 0

            for n in numbers:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        
        ans1 = helper(nums[1:])
        ans2 = helper(nums[:-1])
        
        ans = max(ans1, ans2)

        print(ans)
        return ans