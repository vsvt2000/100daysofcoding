class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack=[]
        node=head
        if node.next==None:
            return True
        while(node.next!=None):
            stack.append(node.val)
            node=node.next
        stack.append(node.val)
        x=""
        for i in stack:
            x=x+str(i)
        if x==x[::-1]:
            return True
        else:
            return False
