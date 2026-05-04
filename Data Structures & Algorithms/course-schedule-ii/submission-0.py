class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        output = []
        visit, cycle = set(), set()
        def dfs(crs): # can this course be completed
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output


        
