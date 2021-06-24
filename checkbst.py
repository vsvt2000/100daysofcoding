arr=[]
def check_binary_search_tree_(root,origin=None):
    if root==None:
        return True
    if origin==None:
        origin=root
    if root.left!=None:
        check_binary_search_tree_(root.left,origin)
    arr.append(root.data)
    if root.right!=None:
        check_binary_search_tree_(root.right,origin)
    if root==origin:
        if arr==sorted(arr) and len(set(arr))==len(arr):
            return True
        else:
            return False
