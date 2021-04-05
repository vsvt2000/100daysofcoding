class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[]
        self.front=-1
        self.rear=-1
        self.maxsize=k
        self.size=0
        for i in range(k):
            self.queue.append(None)
    

    def enQueue(self, value: int) -> bool:
        #print(self.queue,self.front,self.rear)
        if self.size==self.maxsize:
            return False
        if self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=value
            self.size+=1
            return True
        else:
            self.rear=(self.rear+1)%self.maxsize
            self.queue[self.rear]=value
            self.size+=1
            return True
                    
                    
        
            
            
        

    def deQueue(self) -> bool:
        #print(self.queue,self.front,self.rear)
        if self.size==0:
            return False
        else:
            print(self.queue)
            self.queue[self.front]=None
            self.front=(self.front+1)%self.maxsize
            self.size-=1
            return True
        
        

    def Front(self) -> int:
        if self.size==0:
            return -1
        else:
            return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.size==0:
            return -1
        else:
            return self.queue[self.rear]
        
        

    def isEmpty(self) -> bool:
        return self.size==0
        

    def isFull(self) -> bool:
        return self.size==self.maxsize
