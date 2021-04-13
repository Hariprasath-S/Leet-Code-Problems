class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      
      #RECURSIVE
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        res = []
        inorder(root)
        return res
        

        #ITERATIVE
        stack = []
        res = []
        while root or len(stack):
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()         
            res.append(root.val)
            root = root.right
        return res
