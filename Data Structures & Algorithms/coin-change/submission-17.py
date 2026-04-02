class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ways = [float('inf')] * (amount + 1)
        ways[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    ways[a] = min(ways[a], 1 + ways[a - c])
        
        return -1 if ways[amount] == float('inf') else ways[amount]