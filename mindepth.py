class Solution:
    def minDepth(self, root: TreeNode,lens=1) -> int:
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return lens
        res1=None
        res2=None
        
        if root.left!=None:
            res1=self.minDepth(root.left,lens=lens+1)
        if root.right!=None:
            res2=self.minDepth(root.right,lens=lens+1)
        if res1==None:
            return res2
        if res2==None:
            return res1
        else:
            return min(res1,res2)
