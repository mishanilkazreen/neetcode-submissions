class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        neighbours = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbours[pattern].append(word)

        visit, queue = set([beginWord]), deque([beginWord])
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbourWord in neighbours[pattern]:
                        if neighbourWord not in visit:
                            visit.add(neighbourWord)
                            queue.append(neighbourWord)
            res += 1
        return 0