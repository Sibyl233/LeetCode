# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1：双指针
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         m, n = 0, 0
#         p, q = headA, headB
#         while p:
#             m += 1
#             p = p.next
#         while q:
#             n += 1
#             q = q.next
            
#         if m < n: 
#             headA, headB = headB, headA
#             m, n = n, m
#         for i in range(m - n): 
#             headA = headA.next
#         while headA != headB and headA: 
#             headA, headB = headA.next, headB.next

#         if not headA:
#             return None
#         else:
#             return headA

# 解法2：浪漫相遇双指针
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p


