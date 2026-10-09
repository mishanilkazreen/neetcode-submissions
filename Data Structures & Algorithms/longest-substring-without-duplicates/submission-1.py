class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        best = 0

        for j, v in enumerate(s):
            while v in seen:
                seen.remove(s[i])
                i += 1
            seen.add(v)
            best = max(best, j - i + 1)
            
        return best