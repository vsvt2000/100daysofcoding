class Solution:
    def getTree(self, lists:list) -> TreeNode:
        if len(lists)==1:
            x=TreeNode(lists[0])
            return x
        mid=len(lists)//2
        node=TreeNode(lists[mid])
        llists=[]
        rlists=[]
        if mid==len(lists)-1:
            llist=lists[:mid]
            node.left=self.getTree(llist)
            return node
        else:
            llist=lists[:mid]
            rlist=lists[mid+1:]
            node.left=self.getTree(llist)
            node.right=self.getTree(rlist)
            return node
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        node=head
        if node==None:
            return node
        if node.next==None:
            x=TreeNode(node.val)
            return x
        nodelist=[]
        while node.next!=None:
            nodelist.append(node.val)
            node=node.next
        nodelist.append(node.val)
        root=self.getTree(nodelist)
        return root
            
