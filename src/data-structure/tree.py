# 定义
class TreeNode:
    def __init__(self, x):
        self.val = x      # 节点值
        self.left = None  # 左子节点
        self.right = None # 右子节点

# 初始化节点
n1 = TreeNode(3) 
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(1)
n5 = TreeNode(2)

# 构建引用指向
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

from typing import List
def preOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if not node: 
            return node
        # 前序遍历
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    res = []
    dfs(root)
    return res
    

def inOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if not node: 
            return node
        # 中序遍历
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    
    res = []
    dfs(root)
    return res

def postOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if not node: 
            return node
        # 后序遍历
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    
    res = []
    dfs(root)
    return res

import collections
# def levelOrder(root: TreeNode) -> List[int]:
#     res = []
#     queue = collections.deque()
#     queue.append(root)
#     while queue:
#         node = queue.popleft()
#         res.append(node.val)
#         if node.left: queue.append(node.left)
#         if node.right: queue.append(node.right)
#     return res

# # 逐层打印 V1
# def levelOrder(root: TreeNode) -> List[List[int]]:
#     res = []
#     queue = collections.deque()
#     queue.append(root)
#     while queue:
#         tmp = []
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             tmp.append(node.val)
#             if node.left: queue.append(node.left)
#             if node.right: queue.append(node.right)
#         res.append(tmp)
#     return res

# 逐层打印 V2
def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    queue = collections.deque()
    queue.append((root,0))
    while queue:
        node, depth = queue.popleft()
        if depth == len(res):
            res.append([])
        res[depth].append(node.val)
        if node.left: queue.append((node.left, depth+1))
        if node.right: queue.append((node.right, depth+1))
    return res

print("preorder:", preOrder(n1))
print("inorder:", inOrder(n1))
print("postorder:", postOrder(n1))
print("levelorder:", levelOrder(n1))

#     3
#    / \
#   4   5
#  / \
# 1   2




