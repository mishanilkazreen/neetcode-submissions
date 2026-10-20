class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        heap = [(grid[0][0], 0, 0)]

        while heap:
            time_needed, row, col = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if (row, col) == (size - 1, size - 1):
                return time_needed

            for d_row, d_col in directions:
                next_row, next_col = row + d_row, col + d_col
                if (
                    0 <= next_row < size and 0 <= next_col < size and
                    (next_row, next_col) not in visited
                ):
                    next_time = max(time_needed, grid[next_row][next_col])
                    heapq.heappush(heap, (next_time, next_row, next_col))