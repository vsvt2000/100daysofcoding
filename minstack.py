class MinStack:

    def __init__(self):
        self.tops=-1
        self.stack=[]
        self.mina=[]
        self.min=None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.tops+=1
        if self.tops==0:
            self.mina.append(val)
            self.min=val
        else:
            self.mina.append(val)
            self.min=sorted(self.mina)[0]

    def pop(self) -> None:
        self.stack.pop(-1)
        self.mina.pop(-1)
        if len(self.mina)!=0:
            self.min=sorted(self.mina)[0]
        else:
            self.min=None
        self.tops-=1
        

    def top(self) -> int:
        return self.stack[self.tops]
        

    def getMin(self) -> int:
        return self.min
        
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
