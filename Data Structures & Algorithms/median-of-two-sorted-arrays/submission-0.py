class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a                              # binary search on the shorter array

        m, n = len(a), len(b)
        half = (m + n + 1) // 2                      # size of the left half
        lo, hi = 0, m                                # i can be anything from 0 to m

        while lo <= hi:
            i = (lo + hi) // 2                       # elements taken from a for the left half
            j = half - i                             # elements taken from b

            a_left  = a[i - 1] if i > 0 else float("-inf")
            a_right = a[i]     if i < m else float("inf")
            b_left  = b[j - 1] if j > 0 else float("-inf")
            b_right = b[j]     if j < n else float("inf")

            if a_left <= b_right and b_left <= a_right:         # the cut is correct
                if (m + n) % 2:
                    return max(a_left, b_left)                  # odd total: the median is the largest on the left
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            if a_left > b_right:
                hi = i - 1                           # took too many from a
            else:
                lo = i + 1      