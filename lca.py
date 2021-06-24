def lca(root, v1, v2):
    if v1>v2:
        temp=v1
        v1=v2
        v2=temp
    if root.info>=v1 and root.info<v2 or  root.info>v1 and root.info<=v2 or  root.info>v1 and root.info<v2:
        return root
    else:
        if root.info>v1 and root.info>v2:
            if root.left!=None:
                return lca(root.left,v1,v2)
        if root.info<v1 and root.info<v2:
            if root.right!=None:
                return lca(root.right,v1,v2)
