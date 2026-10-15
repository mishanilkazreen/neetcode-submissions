class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        height, width = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append([r, c])

            while queue:
                row, col = queue.popleft()
                distances = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in distances:
                    r, c = dr+row, dc+col

                    if (
                        0 <= r < height and 0 <= c < width and
                        grid[r][c] > grid[row][col] + 1 and
                        grid[r][c] > 0
                        ):
                        grid[r][c] = min(grid[r][c], grid[row][col] + 1)
                        queue.append([r, c])
                
        for r in range(height):
            for c in range(width):
                if (grid[r][c] == 0):
                    bfs(r, c)
