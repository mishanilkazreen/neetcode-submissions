class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit, cycle = set(), set()
        res = []

        def dfs(letter):
            if letter in cycle: return False
            if letter in visit: return True

            cycle.add(letter)
            for nxt in adj[letter]:
                if not dfs(nxt): return False
            cycle.remove(letter)
            visit.add(letter)
            res.append(letter)
            return True

        for letter in adj:
            if not dfs(letter): return ""

        return "".join(reversed(res))   