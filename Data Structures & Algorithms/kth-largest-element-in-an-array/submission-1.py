import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        while True:
            pivot = random.choice(nums)
            hi = [x for x in nums if x > pivot]
            eq = [x for x in nums if x == pivot]
            if k <= len(hi):
                nums = hi
            elif k <= len(hi) + len(eq):
                return pivot
            else:
                k -= len(hi) + len(eq)
                nums = [x for x in nums if x < pivot]