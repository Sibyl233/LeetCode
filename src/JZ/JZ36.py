# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""解法：中序遍历（因为要转换成一个排序的循环双向链表）
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) 
            # 当pre != null时，cur左侧存在节点pre，两者相互指向
            if self.pre: 
                self.pre.right, cur.left = cur, self.pre
            # 当pre == null时，cur左侧没有节点，即此时cur为双向链表中的头节点
            else: 
                self.head = cur
            # 用pre记录上一次迭代中的cur，即双向链表中位于cur左侧的节点
            self.pre = cur 
            dfs(cur.right) 
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head # 头节点和尾节点相互指向
        return self.head