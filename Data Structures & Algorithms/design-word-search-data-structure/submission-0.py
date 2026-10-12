class TriNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TriNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TriNode()
            cur = cur.children[c] 
        cur.isWord = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.isWord
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            if c not in node.children:
                return False
            return dfs(node.children[c], i+1)

        
        return dfs(self.root, 0)


