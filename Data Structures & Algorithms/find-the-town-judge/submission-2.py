class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_dict = {p: 0 for p in range(1, n + 1)}

        for ai, bi in trust:
            trust_dict[ai] -= 1
            trust_dict[bi] += 1

        for key, val in trust_dict.items():
            if val == n - 1:
                return key

        return -1
