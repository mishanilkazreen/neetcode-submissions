class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for num in s:
            # NOTE: Only runs at the start of the sequence
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                best = max(best, length)
        return best

        