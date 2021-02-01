from binarytree import Node as TreeNode, build

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node: 
                return
            dfs(node.right)
            if self.k == 0: 
                return
            self.k -= 1 # 为什么要用self?
            if self.k == 0: 
                self.res = node.val
            dfs(node.left)

        self.k = k
        dfs(root)
        return self.res

if __name__=="__main__": 
    root = [5,3,6,2,4,None,None,1]
    root = build(root)
    k = 3
    print(Solution().kthLargest(root, k)) # 4

