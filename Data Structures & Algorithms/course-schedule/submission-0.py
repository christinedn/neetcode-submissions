class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create preMap
        preMap = {i: [] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)
        # create visitedSet
        visitedSet = set()
        # dfs function
        def dfs(crs): 
            # base case: cycle has been detected, prereq of this course has empty list
            if crs in visitedSet:
                return False
            if preMap[crs] == []:
                return True
            # otherwise, add to visitSet
            visitedSet.add(crs)
            # loop through prereq of the course, and run dfs on that course
            for prereq in preMap[crs]:
                if not dfs(prereq): return False
            visitedSet.remove(crs)
            preMap[crs] = []
            return True
        # if this dfs function returns false at all, we will return false for the algorithm bc we know that all courses cannot be completed
        # otherwise, remove from visitSet and also set the prereq for that course to empty list. 
        # then return true

        # iterate through courses. if not dfs(crs): return false otherwise return true
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        # for case like this: 1 -> 2, 3 -> 4 (they are disconnected)