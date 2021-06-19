class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ele=set()
        node=head
        if node==None:
            return head
        prev=node
        while(node.next!=None):
            if node.val not in ele:
                ele.add(node.val)
                prev=node
                node=node.next
                continue
            else:
                prev.next=node.next
                node.next=None
                node=prev
                node=prev.next
                
        if node.val in ele:
            prev.next=None
        return head
