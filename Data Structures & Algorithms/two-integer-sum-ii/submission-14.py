class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, len(numbers) - 1
        while l < r:
            proposal = numbers[l] + numbers[r]
            
            if proposal == target:
                return [l + 1, r + 1]
            elif proposal > target:
                r -= 1
            
            else:
                l += 1




        return res