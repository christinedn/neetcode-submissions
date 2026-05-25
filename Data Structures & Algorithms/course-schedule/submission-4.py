class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create preMap
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # create visitedSet
        visitSet = set()
        # dfs function
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


                

        # base case: cycle has been detected, prereq of this course has empty list
        # otherwise, add to visitSet
        # loop through prereq of the course, and run dfs on that course
        # if this dfs function returns false at all, we will return false for the algorithm bc we know that all courses cannot be completed
        # otherwise, remove from visitSet and also set the prereq for that course to empty list. 
        # then return true
        # iterate through courses. if not dfs(crs): return false otherwise return true
        # for case like this: 1 -> 2, 3 -> 4 (they are disconnected)