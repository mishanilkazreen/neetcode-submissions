class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = "".join(c.lower() for c in s if c.isalnum())
        print(s_filtered)
        l, r = 0, len(s_filtered)-1
        while l < r:
            if s_filtered[l] != s_filtered[r]:
                return False
            l += 1
            r -= 1
        return True