class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height, width = len(board), len(board[0])
        sub, seen = "", set()

        def dfs(k, r, c, sub, seen):
            if not(0 <= r and r < height and 0 <= c and c < width):
                return False # check if r, c in bounds
            if k == len(word):
                return False # check if substring in bounds
            if (r, c) in seen:
                return False # check if visited
            if board[r][c] != word[k]:
                return False # check to see if char diverges from word

            sub += board[r][c]
            seen.add((r, c))
            if sub == word:
                return True
            
            found = (
                dfs(k+1, r-1, c, sub, seen) or # top
                dfs(k+1, r+1, c, sub, seen) or  # bottom
                dfs(k+1, r, c-1, sub, seen) or # left
                dfs(k+1, r, c+1, sub, seen) # right
                )
                
            seen.remove((r, c))
            return found

        for row in range(height):
            for column in range(width):
                found = dfs(0, row, column, sub, seen)
                if found: return True
        return False