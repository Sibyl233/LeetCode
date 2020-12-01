from typing import List
from utils.listNode import *

# 解法1：双指针
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre, cur = None, head #定义指针
#         while cur:
#             cur.next, pre, cur = pre, cur, cur.next
#         return pre

# 解法2：递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None): return head
        cur = self.reverseList(head.next)
        head.next.next = head #head的下一个节点指向head
        head.next = None
        return cur

if __name__=="__main__": 
    head = listToListNode([1, 2, 3, 4, 5, ])
    printListNode(Solution().reverseList(head))