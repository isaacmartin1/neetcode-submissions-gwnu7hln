from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        target_dict = defaultdict(int)

        for i in range(len(s1)):
            target_dict[s1[i]] += 1

        l = 0

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                l += 1

            iteration_dict = defaultdict(int)

            for i in range(l, r + 1):
                iteration_dict[s2[i]] += 1
            
            if iteration_dict == target_dict:
                return True

            r += 1
        return False