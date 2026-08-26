class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res = 0
        def dfs(node):
            nonlocal res
            if node not in visited:
                visited.add(node)
                for nei in adj[node]:
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        return res

