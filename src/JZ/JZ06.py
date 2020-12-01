from typing import List
from utils.listNode import *

# 解法1：用栈实现
# class Solution:
#     def reversePrint(self, head: ListNode) -> List[int]:
#         stack = []
#         while head:
#             stack.append(head.val)
#             head = head.next
#         return stack[::-1]

# 解法2：递归
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

if __name__=="__main__": 
    head = listToListNode([1, 3, 2])
    printListNode(head)
    print(Solution().reversePrint(head)) # [2, 3, 1]