import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        best = end
        while start <= end:
            mid = (start + end) // 2

            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total <= h:
                best = mid
                end = mid - 1
            else:
                start = mid + 1
        return best
