class MinStack:

    def __init__(self):
        self.main_stk = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        self.main_stk.append(val)

    def pop(self) -> None:
        if self.mins[-1] == self.main_stk[-1]:
           self.mins.pop()
        self.main_stk.pop()
        

    def top(self) -> int:
        return self.main_stk[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
