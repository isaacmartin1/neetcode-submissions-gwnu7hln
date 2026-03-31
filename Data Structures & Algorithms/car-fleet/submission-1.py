class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort car positions
        pairs = [[p, s] for p, s in zip(position, speed)]

        stack = [] # start position, speed, hours to reach
        for p, s in sorted(pairs)[::-1]:
            stack.append((target-p)/s) # gives stack of times to completion
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


            # time_to_destination_per_car = [(target-position[idx])/speed[idx] for idx in range(len(speed))]

        