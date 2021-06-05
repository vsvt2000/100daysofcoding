class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        if head.next==None:
            return head
        nodes=head
        size=1
        while nodes.next!=None:
            nodes=nodes.next
            size+=1
        
        for i in range(k%size):
            node=head
            while(node.next.next!=None):
                node=node.next
            temp=node.next
            node.next=None
            temp.next=head
            head=temp
            
        return head
