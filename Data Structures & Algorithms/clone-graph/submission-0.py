"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if not node or node in visited:
                return visited[node]
            new = Node(node.val)
            visited[node] = new
            for neighbor in node.neighbors:
                if neighbor:
                    new.neighbors.append(dfs(neighbor))
            return new
        return dfs(node) if node else None