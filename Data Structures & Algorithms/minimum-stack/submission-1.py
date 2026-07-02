class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = float("inf")
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.curr_min:
            self.curr_min = val
        self.min_stack.append(self.curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if len(self.min_stack) == 0:
            self.curr_min = float("inf")
        else:
            self.curr_min = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
