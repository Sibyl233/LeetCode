from binarytree import Node as TreeNode

"""解法1：暴力递归
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return self.countNodes(root.left) + self.countNodes(root.right) + 1

"""解法2：
- 时间复杂度：O(log(n)^2)
- 空间复杂度：O(1)
"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftHeight = rightHeight = 0
        leftNode = rightNode = root
        while leftNode:
            leftNode = leftNode.left
            leftHeight += 1
        while rightNode:
            rightNode = rightNode.right
            rightHeight += 1
        if leftHeight == rightHeight:
            return pow(2,leftHeight) - 1
            
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

if __name__=="__main__": 
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right = TreeNode(6)
    print(root)
    print(Solution().countNodes(root)) # 5