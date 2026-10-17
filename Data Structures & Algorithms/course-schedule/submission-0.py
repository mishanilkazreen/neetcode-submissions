class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visit = set()
        def dfs(node):
            if node in visit: return False
            if preMap[node] == []: return True
            
            visit.add(node)
            for pre in preMap[node]:
                if not dfs(pre): return False
            visit.remove(node)
            preMap[node] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course): 
                return False
        return True
