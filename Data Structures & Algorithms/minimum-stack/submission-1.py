class MinStack:

    def __init__(self):
        self.data = []
        
    def push(self, val: int) -> None:
        min_val = min(val, self.data[-1][1]) if self.data else val
        self.data.append((val, min_val))

    def pop(self) -> None:
        if self.data:
            self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1][0]

    def getMin(self) -> int:
        if self.data:
            return self.data[-1][1]