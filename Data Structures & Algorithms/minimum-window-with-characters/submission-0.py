class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s): return ""

        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        have, need = 0, len(count_t)
        best_start, best_len = 0, float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if r-l+1 < best_len:
                    best_start, best_len = l, r-l+1
                
                left = s[l]
                window[left] -= 1

                if left in count_t and window[left] < count_t[left]:
                    have -= 1
                l += 1
            
        return "" if best_len == float("inf") else s[best_start:best_start + best_len]