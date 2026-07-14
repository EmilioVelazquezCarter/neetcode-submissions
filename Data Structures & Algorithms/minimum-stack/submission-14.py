class MinStack:

    def __init__(self):
        self.stack = []
        self.minL = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minL:
            self.minL.append(val)
        else:
            self.minL.append(min(val, self.minL[-1]))
        # if not self.minL:
        #     self.minL.append(val)
        #     index = len(self.minL) -1
        # if self.minL:
        #     index = len(self.minL) -1

        #     lastmin = self.minL[index-1]
        #     print(lastmin)
        # if len(self.minL) > 0 and val < lastmin:
        #     self.minL.append(val)
        #     lastmin = val
        # else: 
        #     self.minL.append(lastmin)
        # print(self.minL)





    def pop(self) -> None:
        self.minL.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minL[-1]
