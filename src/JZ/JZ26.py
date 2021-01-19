from binarytree import Node as TreeNode

"""解法1：递归法
- 时间复杂度：O(MN)。其中 M,N 分别为树 A 和树 B 的节点数量。
- 空间复杂度：O(M)。
"""
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

if __name__=="__main__": 
    A = TreeNode(3)
    A.left = TreeNode(4)
    A.right = TreeNode(5)
    A.left.left = TreeNode(1)
    A.left.right = TreeNode(2)

    B = TreeNode(4)
    B.left = TreeNode(1)

    print(A, B)
    
    print(Solution().isSubStructure(A, B)) 
