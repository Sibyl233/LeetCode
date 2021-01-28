from binarytree import Node as TreeNode
from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, tar):
            if node is None: 
                return
            # 前序遍历
            path.append(node.val) # 记录路径
            tar -= node.val
            if tar == 0 and not node.left and not node.right: # 当目标值减至0，且该节点为叶子节点时得到一条合法路径
                res.append(list(path))
            dfs(node.left, tar)
            dfs(node.right, tar)
            path.pop() # 向上回溯前删除当前路径
    
        res, path = [], []
        dfs(root, sum)
        return res

if __name__=="__main__": 
    sum = 22
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(root)
    print(Solution().pathSum(root, sum)) 

#   [
#    [5,4,11,2],
#    [5,8,4,5]
#   ]