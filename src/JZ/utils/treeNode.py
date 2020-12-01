# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# def listToTreeNode(list):
#     head = ListNode(list[0])
#     p = head
#     for i in range(1, len(list)):
#         p.next = ListNode(list[i])
#         p = p.next
#     return head

# def printTreeNode(TreeNode):
#     if TreeNode != None:
#         print(TreeNode.val)
#         printTreeNode(TreeNode.left)
#         printTreeNode(TreeNode.right)

