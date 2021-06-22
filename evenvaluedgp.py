def sumEvenGrandparent(self, root,par=None,gp=None,s=0):
        if root==None:
            return 0
        if gp!=None:
            if gp.val%2==0:
                #pint(root.val,"added to",s)
                s+=root.val
        
        gp=par
        par=root
        if root.left!=None:
            s+=self.sumEvenGrandparent(root.left,par,gp,0)
        if root.right!=None:
            s+=self.sumEvenGrandparent(root.right,par,gp,0)
        return s
