from binarytree import Node as TreeNode
import collections

"""解法1：先序遍历+判断深度（自顶向下）
- 时间复杂度：O(NlogN)。详见题解。
- 空间复杂度：O(N)。最差情况下，递归深度达到 N 。
"""
# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root: return True
#         return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
#             self.isBalanced(root.left) and self.isBalanced(root.right)

#     # JZ55-I
#     def depth(self, root):
#         if not root: return 0
#         return max(self.depth(root.left), self.depth(root.right)) + 1

"""解法2：后序遍历+剪枝（自底向上）
- 时间复杂度：O(N)。最差情况下，需要遍历树的所有节点。
- 空间复杂度：O(N)。最差情况下，递归深度达到 N 。
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

if __name__=="__main__": 
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(root)
    print(Solution().isBalanced(root)) # True

