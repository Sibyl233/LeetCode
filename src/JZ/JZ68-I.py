from binarytree import Node as TreeNode

"""解法1：迭代
- 时间复杂度：O(N)。其中 N 为二叉树节点数；每循环一轮排除一层，二叉搜索树的层数最小为 logN （满二叉树），最大为 N（退化为链表）。
- 空间复杂度：O(1)。
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val < p.val and root.val < q.val: # p,q 都在 root 的右子树中
                root = root.right # 遍历至右子节点
            elif root.val > p.val and root.val > q.val: # p,q 都在 root 的左子树中
                root = root.left # 遍历至左子节点
            else: break
        return root

"""解法2：递归
- 时间复杂度：O(N)。其中 N 为二叉树节点数；每循环一轮排除一层，二叉搜索树的层数最小为 logN （满二叉树），最大为 N（退化为链表）。
- 空间复杂度：O(N)。最差情况下，递归深度达到 N ，使用 O(N) 大小的额外空间。
"""
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root.val < p.val and root.val < q.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         if root.val > p.val and root.val > q.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         return root

if __name__=="__main__": 
    # root = [6,2,8,0,4,7,9,null,null,3,5]
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    # p = 2
    p = root.left
    # q = 4
    q = root.left.right

    print(root)
    print(Solution().lowestCommonAncestor(root, p, q)) # 2