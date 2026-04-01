class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            # if n == 0:
            #     currMin, currMax = 1, 1
            #     continue

            tmpMax = currMax
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * tmpMax, n * currMin, n)
            res = max(res, currMax, currMin)

        return res

