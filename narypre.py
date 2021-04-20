class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        if root==None:
            return ans
        if root!=None:
            ans.append(root.val)
        for i in root.children:
            if i!=None:
                x=self.preorder(i)
                if len(x)>0:
                    for j in x:
                        ans.append(j)
        return ans
