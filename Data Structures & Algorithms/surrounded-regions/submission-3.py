class Solution:
    def solve(self, board: List[List[str]]) -> None:
        height, width = len(board), len(board[0])
        visit, capture = set(), []

        def bfs(nodes: List[tuple]) -> None:
            queue = deque(nodes)
            visit.update(nodes)

            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc

                    if (
                        0 <= nr < height and 0 <= nc < width and
                        board[nr][nc] == "O" and
                        (nr, nc) not in visit
                        ):
                        queue.append((nr, nc))
                        visit.add((nr, nc))
                    
        for r in range(height):
            for c in range(width):
                if (
                    (r == 0 or r == height-1 or c == 0 or c == width-1) and
                    board[r][c] == "O"
                    ):
                    capture.append((r, c))

        bfs(capture)

        for r in range(height):
            for c in range(width):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"

