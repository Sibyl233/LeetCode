from typing import List
from utils.listNode import *

"""
解法1：自顶向下归并排序（递归）
    - 时间复杂度：O(nlog(n))，n为链表长度
    - 空间复杂度：O(1)
"""
class Solution:
    def sortList(self, head: ListNode) -> List[int]:
        def sort(head: ListNode) -> ListNode:
            # 特例处理
            if not head or not head.next:
                return head
            # 快慢指针法切分链表
            slow, fast = head, head.next # 注意两个指针的起始位置
            while fast and fast.next:    # 当快指针到达链表尾部时退出循环
                slow, fast = slow.next, fast.next.next
            mid = slow.next
            slow.next = None             # 从中间【断开】链表
            # 递归合并
            return merge(sort(head), sort(mid))
            
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            tmp, tmp1, tmp2 = dummyHead, head1, head2
            while tmp1 and tmp2:
                if tmp1.val <= tmp2.val:
                    tmp.next = tmp1
                    tmp1 = tmp1.next
                else:
                    tmp.next = tmp2
                    tmp2 = tmp2.next
                tmp = tmp.next
            if tmp1:
                tmp.next = tmp1
            elif tmp2:
                tmp.next = tmp2
            return dummyHead.next
        
        return sort(head)

"""
解法2：自底向上归并排序（迭代）
    - 时间复杂度：O(nlog(n))，n为链表长度
    - 空间复杂度：O(1)
"""
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:


       
               
                

if __name__=="__main__": 
    head = listToListNode([4, 2, 1, 3])
    printListNode(Solution().sortList(head)) 