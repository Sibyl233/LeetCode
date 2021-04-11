from typing import List
from utils.listNode import *

# 解法1：双指针
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre, cur = None, head #定义指针
#         while cur:
#             cur.next, pre, cur = pre, cur, cur.next
#             # tmp = cur.next
#             # cur.next = pre
#             # pre = cur
#             # cur = tmp
#         return pre

# 解法2：递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre     # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            cur.next = pre             # 修改节点引用指向
            return res                 # 返回反转链表的头节点
        
        return recur(head, None)       # 调用递归并返回

if __name__=="__main__": 
    head = listToListNode([1, 2, 3, 4, 5, ])
    printListNode(Solution().reverseList(head))