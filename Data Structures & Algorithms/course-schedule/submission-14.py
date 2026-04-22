class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            # base case: empty array, meaning can complete the course
            if preMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # if we're able to complete all pre of the course..
            visiting.remove(crs) # remove from visited since we are done with our path
            preMap[crs] = []
            return True

        for crs in preMap:
            if not dfs(crs):
                return False
        return True