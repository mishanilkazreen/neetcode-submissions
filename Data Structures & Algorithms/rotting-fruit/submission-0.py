class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        height, width = len(grid), len(grid[0])

        for r in range(height):
            for c in range(width):
                if grid[r][c] == 2:
                    queue.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        mins = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc

                    if (
                        0 <= r < height and 0 <= c < width and
                        grid[r][c] == 1
                        ):
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append([r, c])
            mins += 1
        return mins if fresh == 0 else -1
