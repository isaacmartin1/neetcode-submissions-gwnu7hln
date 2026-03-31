class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_dict = {p: 0 for p in range(1, n + 1)}

        ai_set = set()

        for ai, bi in trust:
            ai_set.add(ai)
            trust_dict[bi] += 1

        for key, val in trust_dict.items():
            if val == n - 1 and key not in ai_set:
                return key

        return -1