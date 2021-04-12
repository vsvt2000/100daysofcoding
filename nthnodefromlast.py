class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node1=head
        j=1
        while node1.next!=None:
            node1=node1.next
            j+=1
        target=j-n
        i=0
        if target==0:
            head=head.next
            return head
        node2=head
        while node2.next!=None:
            if i==target-1:
                node3=node2.next
                #print(node3.val,node2.val)
                node2.next=node3.next
               #print(node2.next.val)
                node3.next=None
                del node3
                break
            i+=1
            node2=node2.next
        return head
