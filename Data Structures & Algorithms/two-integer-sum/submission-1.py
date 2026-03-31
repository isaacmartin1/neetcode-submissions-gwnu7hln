class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        index = 0
        for value in nums:
            nums_dict[value] = index
            index += 1

        index = 0
        for value in nums:
            difference = target - value
            if difference in nums_dict:
                if nums_dict[difference] != index:
                    j = nums_dict[difference]
                    i = index
            index += 1
        if i < j:
            return [i, j]
        else:
            return [j, i]
