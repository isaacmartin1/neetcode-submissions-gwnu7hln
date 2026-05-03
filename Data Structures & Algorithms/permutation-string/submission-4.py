from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        target_dict = defaultdict(int)

        for i in range(len(s1)):
            target_dict[s1[i]] += 1

        l = 0
        print(target_dict)

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                l += 1
            
            # if s2[l:r + 1] == s1:
            #     return True
            iteration_copy = target_dict.copy()

            for i in range(l, r + 1):
                curr_key = s2[i]
                # curr_val = iteration_copy[curr_key].get()
                iteration_copy[curr_key] -= 1
            print(iteration_copy)
            
            match_found = True
            for val in iteration_copy.values():
                if val != 0:
                    match_found = False

            if match_found:
                return True

            r += 1
        return False