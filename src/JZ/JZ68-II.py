from binarytree import Node as TreeNode

"""解法：递归
- 时间复杂度：O(N)。其中 N 为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
- 空间复杂度：O(N)。最差情况下，递归深度达到 N ，系统使用 O(N) 大小的额外空间。
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: 
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if root == p or root == q: return root
        if not left: return right
        if not right: return left

        return root

if __name__=="__main__": 
    # root = [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    # p = 5
    p = root.left
    # q = 4
    q = TreeNode(4)

    print(root)
    print(Solution().lowestCommonAncestor(root, p, q)) # 5