class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, total = nums[0], 0
        for num in nums:
            if total < 0:
                total = 0
            total += num
            best = max(best, total)
        return best