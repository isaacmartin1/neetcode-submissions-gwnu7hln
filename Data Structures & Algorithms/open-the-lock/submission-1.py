class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        idx_opts = range(4)
        delta_opts = [-1, 1]
        visited = set()
        for d in deadends:
            visited.add(d)
        visited.add('0000')
        def bfs(q):
            while q:
                wheels, depth = q.popleft()
                
                for idx in idx_opts:
                    for d in delta_opts:
                        proposed_wheel = wheels
                        new_val = (int(wheels[idx]) + d) % 10
                        proposed_wheel = wheels[:idx] + str(new_val) + wheels[idx+1:]
                        if proposed_wheel == target:
                            return depth
                        elif proposed_wheel not in visited:
                            visited.add(proposed_wheel)
                            q.append((proposed_wheel, depth + 1))
            return -1

        q = collections.deque()
        q.append(('0000', 1))
        res = bfs(q)

        return res

