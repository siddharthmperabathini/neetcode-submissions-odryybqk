class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = defaultdict(list)
        for p,c in prerequisites:
            hm[c].append(p)
        visited = set()
        def dfs(course):
            if hm[course] == []:
                return True
            visited.add(course)
            for p in hm[course]:
                if p in visited:
                    return False
                if dfs(p) == False:
                    return False
            visited.remove(course)
            hm[course] = []
            return True
        done = set()
        for course in list(hm.keys()):
            if course not in done:
                if dfs(course) == False:
                    return False
        return True
