from binarytree import Node as TreeNode
from typing import List
import collections

"""解法1：层序遍历+双端队列
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: return []
#         res, deque = [], collections.deque([root])
#         while deque:
#             tmp = collections.deque()
#             for _ in range(len(deque)):
#                 node = deque.popleft()
#                 if len(res) % 2: 
#                     tmp.appendleft(node.val) # 偶数层 -> 队列头部
#                 else: 
#                     tmp.append(node.val) # 奇数层 -> 队列尾部
#                 if node.left: deque.append(node.left)
#                 if node.right: deque.append(node.right)
#             res.append(list(tmp))
#         return res

"""解法2：层序遍历+倒序
- 时间复杂度：O(N)
- 空间复杂度：O(N)
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res

if __name__=="__main__": 
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(root)
    print(Solution().levelOrder(root)) 

