class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l = 0
        r = len(people) - 1

        while l <= r:
            remaining_capacity = limit - people[r]
            res += 1
            r -= 1
            if l <= r and people[l] <= remaining_capacity:
                l += 1
        
        return res