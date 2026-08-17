class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
        graph = [set() for i in range(numCourses)]
        def dfs(start, cur, visited):
            for nei in adj[cur]:
                if nei not in visited:
                    visited.add(nei)
                    graph[start].add(nei)
                    dfs(start,nei,visited)
        for course in range(numCourses):
            dfs(course,course,set())
        return [v in graph[u] for u,v in queries]