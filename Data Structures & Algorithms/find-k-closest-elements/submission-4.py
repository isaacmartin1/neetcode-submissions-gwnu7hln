class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while (r - l + 1) > k:
            l_dist = arr[l] - x
            r_dist = arr[r] - x

            if abs(l_dist) > abs(r_dist):
                l += 1
            else:
                r -= 1
        
        return arr[l:r+1]