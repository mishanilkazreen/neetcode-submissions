class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1
        while start <= end:
            mid = (end + start) // 2
            data = matrix[mid // cols][mid % cols]
            if data < target:
                start = mid + 1
            elif data > target:
                end = mid - 1
            else:
                return True
        return False