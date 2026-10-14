class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        seen, islands = set(), 0

        def bfs(r, c):
            queue = deque()
            seen.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (
                        r in range(height) and
                        c in range(width) and
                        grid[r][c] == "1" and
                        (r, c) not in seen
                        ):
                        queue.append((r, c))
                        seen.add((r, c))



        for row in range(height):
            for column in range(width):
                if grid[row][column] == "1" and (row, column) not in seen:
                    bfs(row, column)
                    islands += 1
        return islands
