class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for c in s:
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] += 1
        
        for c in t:
            if c in chars:
                if chars[c] > 1:
                    chars[c] -= 1
                else:
                    chars.pop(c)
            else:
                return False
        
        if len(chars) > 0:
            return False
        return True
                