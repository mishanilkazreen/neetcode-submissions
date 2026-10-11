class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        best = 0
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                L = stack[-1] if stack else -1
                best = max(best, h * (i - L - 1))
            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            L = stack[-1] if stack else -1
            best = max(best, h * (n - L - 1))
        return best