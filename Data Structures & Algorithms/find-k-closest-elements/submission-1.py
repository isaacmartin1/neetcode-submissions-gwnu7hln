class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        self.res = []
        self.diff = []

        for idx in range(len(arr)):
            if len(self.res) < k:
                self.res.append(arr[idx])
                self.diff.append(abs(arr[idx] - x))
            else:
                l = 0
                r = len(self.diff) - 1

                proposed_new_diff = abs(x - arr[idx])

                l_diff = self.diff[l]
                r_diff = self.diff[r]

                if proposed_new_diff < l_diff or proposed_new_diff < r_diff:
                    if l_diff > r_diff:
                        self.res.pop(0)
                        self.diff.pop(0)
                    else:
                        self.res.pop()
                        self.diff.pop()
                    self.diff.append(proposed_new_diff)
                    self.res.append(arr[idx])

        
        return self.res
