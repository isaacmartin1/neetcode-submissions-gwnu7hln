class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        items = defaultdict(list)
        for first, second in edges:
            items[first].append(second)
            items[second].append(first)
        visited = set()

        def dfs(node, l, visited):
            visited.add(node)
            nxt_vals = items[node]
            for v in nxt_vals:
                if v not in visited:
                    dfs(v, l + 1, visited)

        res = 0
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node, 0, visited)
        
        return res
        