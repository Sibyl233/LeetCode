# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1：单指针
# class Solution:
#     def deleteNode(self, head: ListNode, val: int) -> ListNode:
#         if head.val == val: return head.next    #特例处理
#         cur = head #初始化
#         while cur.next and cur.next.val != val: #定位节点
#             cur = cur.next #遍历
#         if cur: cur.next = cur.next.next        #删除节点
#         return head

# 解法2：双指针
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next #特例处理
        pre, cur = head, head.next #初始化
        while cur and cur.val != val:        #定位节点
            pre, cur = cur, cur.next #遍历
        if cur: pre.next = cur.next          #删除节点
        return head

def listToListNode(list):
    head = ListNode(list[0])
    p = head
    for i in range(1, len(list)):
        p.next = ListNode(list[i])
        p = p.next
    return head

def printListNode(ListNode):
    p = ListNode
    while p != None:
        print(p.val, '->', end='')
        p = p.next
    print('NULL')

if __name__=="__main__": 
    head = listToListNode([4,5,1,9])
    val = 5
    printListNode(Solution().deleteNode(head, val))