class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for elem in prerequisites:
            crs, prereq = elem
            preMap[crs].append(prereq)
        
        visited = set()
        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for prereq in preMap[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        for crs in preMap:
            if not dfs(crs): # go through all the courses and ensure that it can be completed
                return False
        return True

