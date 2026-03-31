class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs = sorted(pairs)[::-1] # descending sort

        stack = []
        for p, s in pairs:
            time_to_complete = (target - p) / s
            stack.append(time_to_complete)
            if stack and len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        
        return len(stack)
