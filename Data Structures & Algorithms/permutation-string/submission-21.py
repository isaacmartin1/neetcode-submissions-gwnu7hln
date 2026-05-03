from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        target_dict = defaultdict(int)

        l = 0

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                l += 1


            if sorted(s1) == sorted(s2[l: r + 1]):
                return True

            r += 1
        return False
