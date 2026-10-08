class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temperate in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < temperate:
                    val = stack.pop()
                    result[val[1]] = i-val[1]                   
            stack.append((temperate, i))
        return result