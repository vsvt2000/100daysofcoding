class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None:
            root=TreeNode(val)
            return root
        else:
            if root.val>val:
                if root.left==None:
                    root.left=TreeNode(val)
                else:
                    self.insertIntoBST(root.left,val)
            if root.val<val:
                if root.right==None:
                    root.right=TreeNode(val)
                else:
                    self.insertIntoBST(root.right,val)
            return root
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root=TreeNode(preorder[0])
        preorder.pop(0)
        for i in preorder:
            self.insertIntoBST(root,i)
        return root
        
