class MyQueue:

    def __init__(self):
        self.stack=[]
        self.top=-1
        self.otop=-1
        

    def push(self, x: int) -> None:
        if self.top==self.otop:
            self.stack.append(x)
            self.top+=1
            self.otop+=1
            return
        else:
            self.top+=1
            self.stack[self.top]=x
            return
        

    def pop(self) -> int:
        if self.top!=-1:
            temp=self.stack.pop(0)
            self.top-=1
            self.otop-=1
            return temp
        

    def peek(self) -> int:
        if self.top!=-1:
            return self.stack[0]
        

    def empty(self) -> bool:
        return self.top==-1
