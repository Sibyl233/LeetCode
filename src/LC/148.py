from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
解法1：自顶向下归并排序（递归）
    - 时间复杂度：O(nlog(n))，n为链表长度
    - 空间复杂度：O(1)
"""
# class Solution:
#     def sortList(self, head: ListNode) -> List[int]:
#         def sort(head: ListNode, tail: ListNode) -> ListNode:
#             if not head:
#                 return head
#             if head.next == tail:
#                 head.next = None
#                 return head
#             slow = fast = head
#             while fast != tail:
#                 slow, fast = slow.next, fast.next
#                 if fast != tail:
#                     fast = fast.next
#             mid = slow
#             return merge(sort(head, mid), sort(mid, tail))
            
#         def merge(head1: ListNode, head2: ListNode) -> ListNode:
#             dummyHead = ListNode(0)
#             temp, temp1, temp2 = dummyHead, head1, head2
#             while temp1 and temp2:
#                 if temp1.val <= temp2.val:
#                     temp.next = temp1
#                     temp1 = temp1.next
#                 else:
#                     temp.next = temp2
#                     temp2 = temp2.next
#                 temp = temp.next
#             if temp1:
#                 temp.next = temp1
#             elif temp2:
#                 temp.next = temp2
#             return dummyHead.next
        
#         return sort(head, None)

"""
解法2：自底向上归并排序（迭代）
    - 时间复杂度：O(nlog(n))，n为链表长度
    - 空间复杂度：O(1)
"""
                
          
                
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
    head = listToListNode([4, 2, 1, 3])
    printListNode(Solution().sortList(head)) 