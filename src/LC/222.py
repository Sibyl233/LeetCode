from utils.treeNode import *
from binarytree import Node

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

if __name__=="__main__": 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right = Node(6)
    print(Solution().countNodes(root)) 