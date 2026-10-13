class TriNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TriNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # add words to trie
        root = TriNode()
        for word in words:
            root.addWord(word)

        res, seen = set(), set()
        width, height = len(board[0]), len(board)

        def dfs(i, j, node, word):
            if i < 0 or i >= height or j < 0 or j >= width:
                # out of bounds
                return
            if (i, j) in seen or board[i][j] not in node.children:
                # unique membership only + see if letter is in word
                return
            
            seen.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.isWord:
                res.add(word)

            # top
            dfs(i-1, j, node, word)
            # bottom
            dfs(i+1, j, node, word)
            # left
            dfs(i, j-1, node, word)
            # right
            dfs(i, j+1, node, word)
            seen.remove((i, j))
        
        for row in range(height):
            for column in range(width):
                dfs(row, column, root, "")

        return list(res)