from typing import List
from utils.listNode import *

"""
解法1：自顶向下归并排序（递归）
    - 时间复杂度：O(nlog(n))，n为链表长度
    - 空间复杂度：O(1)
"""
# class Solution:
#     def sortList(self, head: ListNode) -> List[int]:
#         def sort(head: ListNode) -> ListNode:
#             # 特例处理
#             if not head or not head.next: # 处理空链表和单节点的情况
#                 return head
#             # 快慢指针法切分链表
#             slow, fast = head, head.next  # 注意两个指针的起始位置
#             while fast and fast.next:     # 当快指针到达链表尾部时退出循环
#                 slow, fast = slow.next, fast.next.next
#             mid = slow.next
#             slow.next = None              # 确保从中间断开链表！
#             # 递归合并
#             return merge(sort(head), sort(mid))
            
#         def merge(head1: ListNode, head2: ListNode) -> ListNode:
#             tmp = dummyHead = ListNode(0)
#             while head1 and head2:
#                 if head1.val < head2.val:
#                     tmp.next = head1
#                     head1 = head1.next
#                 else:
#                     tmp.next = head2
#                     head2 = head2.next
#                 tmp = tmp.next
#             tmp.next = head1 or head2
#             return dummyHead.next
                    
#         return sort(head)

"""
解法2：自底向上归并排序（迭代）
    - 时间复杂度：O(nlog(n))，n为链表长度
    - 空间复杂度：O(1)
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        cur = head
        length, subLength = 0, 1
        while cur: 
            cur = cur.next
            length = length + 1 # 记录链表长度
        dummyHead = ListNode(0)
        dummyHead.next = head
        
        # 用迭代方式合并子链表
        while subLength < length:
            tmp, cur = dummyHead, dummyHead.next
            while cur:
                # 获取需要归并的两个子链表及其长度
                head1 = cur
                l = subLength
                while l and cur: 
                    cur = cur.next
                    l = l - 1
                if l: 
                    break # 边界条件：链表剩余元素 <= subLength

                head2 = cur
                l = subLength
                while l and cur: 
                    cur = cur.next
                    l = l - 1
                len1, len2 = subLength, subLength - l # 边界条件：subLength < 链表剩余元素 <= subLength*2
                
                # 合并环节
                while len1 and len2:
                    if head1.val < head2.val: 
                        tmp.next = head1
                        head1 = head1.next
                        len1 = len1-1
                    else: 
                        tmp.next = head2
                        head2 = head2.next
                        len2 = len2-1
                    tmp = tmp.next
                tmp.next = head1 if len1 else head2
                
                
                while len1 > 0 or len2 > 0: 
                    tmp = tmp.next
                    len1, len2 = len1 - 1, len2 - 1
                tmp.next = cur 
            
            subLength *= 2

        return dummyHead.next

       
               
                

if __name__=="__main__": 
    head = listToListNode([4, 2, 1, 3])
    printListNode(Solution().sortList(head)) 