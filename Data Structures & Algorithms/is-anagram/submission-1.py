class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        
        for c in t:
            if chars.get(c, 0) == 0:
                return False
            chars[c] -= 1
        return True
                