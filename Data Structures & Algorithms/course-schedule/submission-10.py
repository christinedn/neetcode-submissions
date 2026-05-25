class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            crs, prereq = prereq
            preMap[crs].append(prereq)

        visited = set()
        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True


        for crs in preMap:
            if not dfs(crs):
                return False
        return True