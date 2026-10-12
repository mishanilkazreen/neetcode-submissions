class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for c in s1:
            s1Count[ord(c) - ord('a')] += 1

        for j in range(len(s2)):
            s2Count[ord(s2[j]) - ord('a')] += 1
            if j >= len(s1):
                s2Count[ord(s2[j - len(s1)]) - ord('a')] -= 1
            if s1Count == s2Count: return True
        return False