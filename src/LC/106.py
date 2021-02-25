from typing import List
from binarytree import Node as TreeNode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        #边界条件
        if len(postorder) == 0: return None
        
        #记录中序每个值的下标
        dic = {}
        for i,val in enumerate(inorder):
            dic[val] = i
        
        def dfs(lpost,rpost,lin,rin):
            #边界条件
            if lpost > rpost: return None
            if lpost == rpost:
                return TreeNode(postorder[lpost])
            
            #后序的最后一个值是根节点
            root = TreeNode(postorder[rpost])
            #取出中序的根节点
            idx = dic[root.val]
            
            #递归左右子树
            leftTree = dfs(lpost,lpost+(idx-lin)-1,lin,idx-1)
            rightTree = dfs(lpost+(idx-lin),rpost-1,idx+1,rin)
            #连回根节点
            root.left = leftTree
            root.right = rightTree
            return root

        return dfs(0,len(postorder)-1,0,len(inorder)-1)

if __name__=="__main__": 
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    print(Solution().buildTree(inorder, postorder)) 