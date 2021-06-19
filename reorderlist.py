class Solution:
    def reorderList(self, head: ListNode) -> None:
        check={}
        if head==None:
            return head
        count=0
        while(head.next!=None):
            check[count]=head
            head=head.next
            check[count].next=None
            count+=1
        
        check[count]=head
        #print(count,head)
        node=check[0]
        count=len(check)-1
        count1=1
        for i in range(len(check)-1):
            #print(node.val)
            if i%2==0:
                #print(node.val,count,i,check[count].val,"4here")
                node.next=check[count]
                node=node.next
                count-=1
                continue
            else:
                #print(node.val,count,i,check[count1].val,"here")
                node.next=check[count1]
                count1+=1
                node=node.next
                continue
        #print("final",node.val)
        node.next=None
        return check[0]
