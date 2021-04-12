class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd=[]
        even=[]
        node1=head
        if node1==None:
            return None
        j=0
        while(node1.next!=None):
            if j%2==0:
                odd.append(node1.val)
            else:
                even.append(node1.val)
            j+=1
            node1=node1.next
        if j%2==0:
            odd.append(node1.val)
        else:
            even.append(node1.val)
        for i in even:
            odd.append(i)
        node2=head
        j=0
        while(node2.next!=None):
            node2.val=odd[j]
            j+=1
            node2=node2.next
        node2.val=odd[j]
        return head
