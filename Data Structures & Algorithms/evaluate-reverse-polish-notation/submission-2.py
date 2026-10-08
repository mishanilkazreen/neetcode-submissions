class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+':lambda a, b: a+b,
            '-':lambda a, b: a-b,
            '*':lambda a, b: a*b,
            '/':lambda a, b: int(a/b)}

        for token in tokens:
            if token in operations:
                # token : operator 
                num2 = stack.pop()
                num1 = stack.pop()

                res = operations[token](num1, num2)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]
        