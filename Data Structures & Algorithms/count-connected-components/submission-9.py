class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_dict = defaultdict(list)

        for f, s in edges:
            edge_dict[f].append(s)
            edge_dict[s].append(f)
        
        res = 0

        def dfs(node, visited):
            visited.add(node)
            next_val = edge_dict[node]

            for val in next_val:
                if val not in visited:
                    dfs(val, visited)
        visited = set()
        res = 0
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node, visited)
        return res