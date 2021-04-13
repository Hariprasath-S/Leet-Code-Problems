class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while root or len(stack):
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()         
            root = root.right
        return res
