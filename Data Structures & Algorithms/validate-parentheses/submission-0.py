class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for c in s:
            if c in parentheses:
                if not stack or parentheses[c] != stack[len(stack)-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
            
