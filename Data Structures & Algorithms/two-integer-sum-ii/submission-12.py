class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            proposal = numbers[l] + numbers[r]

            if proposal > target:
                r -= 1
            
            elif proposal < target:
                l += 1
            
            elif proposal == target:
                return [l + 1, r + 1]
        
        return []
