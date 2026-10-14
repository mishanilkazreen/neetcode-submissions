class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, string = [], ""

        def dfs(string, open_count, close_count):
            if open_count + close_count == 2*n:
                res.append(string)
                return

            if open_count < n:
                dfs(string + "(", open_count + 1, close_count)
                
            if close_count < open_count:
                dfs(string + ")", open_count, close_count + 1)

        
        dfs(string, 0, 0)
        return res