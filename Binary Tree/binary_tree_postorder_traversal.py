class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
      
      #RECURSIVE
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
        res = []
        postorder(root)
        return res
        
        #ITERATIVE
        stack = []
        res = []
        p = root
        while stack or p:        
            if p:
                stack.append(p)
                res.append(p.val)
                p = p.right
            else:
                r = stack.pop()
                p = r.left
        return res
        
