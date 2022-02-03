# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        mid=len(nums)//2
        try:
            lnum=nums[:mid]
        except:
            lnum=[]
        try:
            rnum=nums[mid+1:]
        except:
            rnum=[]
        #print(mid)
        if len(nums)>0:
            midnode=TreeNode(nums[mid])
        else:
            return None
        midnode.left=self.sortedArrayToBST(lnum)
        midnode.right=self.sortedArrayToBST(rnum)
        return midnode
        
        
