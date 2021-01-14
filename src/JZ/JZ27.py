
from binarytree import Node as TreeNode

"""解法1：递归法
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: 
            return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root

"""解法2：辅助栈
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
# class Solution:
#     def mirrorTree(self, root: TreeNode) -> TreeNode:
#         if not root: 
#             return
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node.left: 
#                 stack.append(node.left)
#             if node.right: 
#                 stack.append(node.right)
#             node.left, node.right = node.right, node.left
#         return root

if __name__=="__main__": 
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(root)
    print(Solution().mirrorTree(root)) 
