class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preReq = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preReq[course].append(pre)

        visit, cycle = set(), set()
        res = []
        def dfs(node):
            if node in cycle: return False
            if node in visit: return True

            cycle.add(node)
            for pre in preReq[node]:
                if not dfs(pre): return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        for course in range(numCourses):
            if not dfs(course): return []
        return res
