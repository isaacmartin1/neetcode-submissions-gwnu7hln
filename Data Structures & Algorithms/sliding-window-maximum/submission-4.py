from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for r in range(len(nums)):
            # 3: 200
            # receiving idx 3: 200
            # look at the actual values at the indexes for 0, 1, 2
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # this if statement gets rid of indices which are no longer valid
            if r - q[0] >= k:
                q.popleft()

            if r >= k - 1:
                res.append(nums[q[0]])

        return res