class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height, width = len(heights), len(heights[0])

        def bfs(starts):
            queue = deque(starts)
            visit = set(starts)

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < height and 0 <= nc < width and
                        (nr, nc) not in visit and
                        heights[nr][nc] >= heights[row][col]
                        ):
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            return visit

        pacific = [(0, c) for c in range(width)] + [(r, 0) for r in range(height)]
        atlantic = [(height - 1, c) for c in range(width)] + [(r, width - 1) for r in range(height)]

        pac, atl = bfs(pacific), bfs(atlantic)

        return [[r, c] for r, c in pac & atl]