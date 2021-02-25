from binarytree import Node as TreeNode
import collections

"""解法1：后序遍历
- 时间复杂度：O(N)。其中 N 为二叉树节点数；最差情况下，需要递归遍历树的所有节点。
- 空间复杂度：O(N)。最差情况下，递归深度达到 N 。
"""
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root: return 0
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

"""解法2：层序遍历
- 时间复杂度：O(N)。其中 N 为二叉树节点数；最差情况下，需要遍历树的所有节点。
- 空间复杂度：O(N)。最差情况下（当树平衡时），队列 queue 同时存储 N/2 个节点。
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append((root,0))
        while queue:
            node, depth = queue.popleft()
            if node.left: queue.append((node.left, depth+1))
            if node.right: queue.append((node.right, depth+1))
        return depth+1

if __name__=="__main__": 
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(root)
    print(Solution().maxDepth(root)) # 3

