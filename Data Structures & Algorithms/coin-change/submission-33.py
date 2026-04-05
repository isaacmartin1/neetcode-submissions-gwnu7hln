class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opts = [float('inf')] * (amount + 1)
        opts[0] = 0
        for a in range(0, amount + 1):
            for c in coins:
                if a - c >= 0:
                    opts[a] = min(opts[a], 1 + opts[a - c])

        return opts[amount] if opts[amount] != float('inf') else -1
