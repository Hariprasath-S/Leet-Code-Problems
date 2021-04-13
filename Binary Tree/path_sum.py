class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and root.val == targetSum: return True
        targetSum -= root.val
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum) 
