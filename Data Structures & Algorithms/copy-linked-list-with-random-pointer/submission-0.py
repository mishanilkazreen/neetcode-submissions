"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.map = {None: None}

        cur = head
        while cur:
            tmp = Node(cur.val)
            self.map[cur] = tmp
            cur = cur.next

        cur = head
        while cur:
            tmp = self.map[cur]
            tmp.next = self.map[cur.next]
            tmp.random = self.map[cur.random]
            cur = cur.next
        return self.map[head]
        
        return cur