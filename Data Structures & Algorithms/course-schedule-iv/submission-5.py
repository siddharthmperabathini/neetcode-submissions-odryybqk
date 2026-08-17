from typing import List

class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)

        reachable = [set() for _ in range(numCourses)]

        def dfs(start: int, node: int, visited: set) -> None:
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    reachable[start].add(neighbor)
                    dfs(start, neighbor, visited)

        # Compute all direct and indirect reachable courses
        for course in range(numCourses):
            dfs(course, course, set())

        # Each lookup is O(1) on average
        return [v in reachable[u] for u, v in queries]