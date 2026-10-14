class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0

        height, width = len(grid), len(grid[0])
        best = 0

        def bfs(r, c):
            queue = deque()

            grid[r][c] = 0
            queue.append((r, c))
            islands = 1

            while queue:
                row, column = queue.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, column + dc

                    if (
                        r in range(height) and
                        c in range(width) and
                        grid[r][c] == 1
                        ):
                        queue.append((r, c))
                        grid[r][c] = 0
                        islands += 1 
            return islands

        for row in range(height):
            for column in range(width):
                if grid[row][column] == 1:
                    islands = bfs(row, column)
                    best = max(best, islands)
        return best