class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        for n in nums:
            tmpMax = currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * tmpMax, n * currMin, n)
            res = max(currMax, res)
        
        return res