class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start, best_len = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                start, length = expand(left, right)
                if length > best_len:
                    best_start, best_len = start, length

        return s[best_start:best_start + best_len]