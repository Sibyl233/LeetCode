from utils.listNode import *

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

if __name__=="__main__": 
    head = listToListNode([4,5,1,9])
    val = 5
    printListNode(Solution().deleteNode(head, val))