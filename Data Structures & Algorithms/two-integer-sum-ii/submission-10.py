class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        for first_idx in range(len(numbers)):
            for second_idx in range(len(numbers)):
                first_n = numbers[first_idx]
                second_n = numbers[second_idx]
                if first_n != second_n:
                    if first_n + second_n == target:
                        return [first_idx + 1, second_idx + 1]
        
        return []
        