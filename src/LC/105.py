from typing import List
from binarytree import Node as TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #边界条件
        if len(preorder) == 0: return None
        
        #记录中序每个值的下标
        dic = {}
        for i,val in enumerate(inorder):
            dic[val] = i
        
        def dfs(lpre,rpre,lin,rin):
            #边界条件
            if lpre > rpre: return None
            if lpre == rpre:
                return TreeNode(preorder[lpre])
            
            #前序的第一个值是根节点
            root = TreeNode(preorder[lpre])
            #取出中序的根节点
            idx = dic[root.val]
            
            #递归左右子树
            leftTree = dfs(lpre+1,lpre+(idx-lin),lin,idx-1)
            rightTree = dfs(lpre+(idx-lin)+1,rpre,idx+1,rin)
            #连回根节点
            root.left = leftTree
            root.right = rightTree
            return root

        return dfs(0,len(preorder)-1,0,len(inorder)-1)

if __name__=="__main__": 
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(Solution().buildTree(preorder, inorder)) 