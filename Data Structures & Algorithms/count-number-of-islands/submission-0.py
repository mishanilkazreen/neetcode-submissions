class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        seen, count = set(), 0

        def dfs(r, c):
            if not(0 <= r < height and 0 <= c < width):
                # out of bounds
                return 0 
            if (r, c) in seen:
                # check if visited
                return 0
            if grid[r][c] == "0":
                return 0
            
            seen.add((r, c))

            dfs(r-1, c)  # top
            dfs(r+1, c)  # bottom
            dfs(r, c-1)  # left
            dfs(r, c+1)  # right

            return 1

        for row in range(height):
            for column in range(width):
                count += dfs(row, column)

        return count
