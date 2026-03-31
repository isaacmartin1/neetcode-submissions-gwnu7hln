class Solution:
    def rob(self, nums: List[int]) -> int:
        house_1, house_2 = 0, 0

        for n in nums:
            temp = max(house_1 + n, house_2)
            house_1 = house_2
            house_2 = temp
        
        return house_2
