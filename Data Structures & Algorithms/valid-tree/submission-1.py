class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False
        visit = set()
        adj = [[] for i in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        def dfs(node,parent):
            if node in visit:
                return False                        
            visit.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei,node) == False:
                    return False
            return True
        return dfs(0,-1) and len(visit) == n