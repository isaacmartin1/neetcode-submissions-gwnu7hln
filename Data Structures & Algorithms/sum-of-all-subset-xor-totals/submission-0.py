class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        combinations = []
        c = []
        max_depth = 2
        def dfs(i):
            if i == len(nums):
                combinations.append(c[:])
                return            
            added_num = nums[i]
            c.append(added_num)
            dfs(i + 1)

            c.pop()
            dfs(i + 1)
        
        dfs(0)
        print(combinations)

        res = 0 
        for sublist in combinations:
            xor_val = 0
            for num in sublist:
                xor_val ^= num
            res += xor_val

        return res
        
