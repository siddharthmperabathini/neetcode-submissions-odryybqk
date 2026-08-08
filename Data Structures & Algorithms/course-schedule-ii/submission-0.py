class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited, cycle = set(),set()

        hm = defaultdict(list)
        for c,p in prerequisites:
            hm[c].append(p)
        

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            cycle.add(c)
            for p in hm[c]:
                if dfs(p) == False:
                    return False
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
