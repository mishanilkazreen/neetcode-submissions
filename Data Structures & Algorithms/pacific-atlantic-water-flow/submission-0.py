class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height, width = len(heights), len(heights[0])
        res = []

        def bfs(r, c):
            queue = deque()
            queue.append([r, c])
            visit = {(r, c)}
            isAtlantic, isPacific = False, False

            while queue and not (isAtlantic and isPacific):
                row, col = queue.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if (
                        (0 <= nr < height and 0 <= nc < width) and
                        heights[nr][nc] <= heights[row][col] and
                        (nr, nc) not in visit
                        ):
                        queue.append([nr, nc])
                        visit.add((nr, nc))

                    if nr < 0 or nc < 0:
                        isPacific = True
                    if nr >= height or nc >= width:
                        isAtlantic = True
            
            if isAtlantic and isPacific:
                res.append([r, c])
        
        for r in range(height):
            for c in range(width):
                bfs(r, c)

        return res