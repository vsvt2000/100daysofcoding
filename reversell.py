class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node=head
        arr=[]
        if head==None:
            return None
        while(node.next!=None):
            x=node
            node=node.next
            x.next=None
            arr.append(x)
        head=node
        node1=head
        while(len(arr)>0):
            node1.next=arr.pop(-1)
            node1=node1.next
        return head
