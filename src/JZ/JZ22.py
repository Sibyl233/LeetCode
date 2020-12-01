from utils.listNode import *

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head #初始化：前、后节点都指向头结点
        for _ in range(k):          #构建双指针距离：前节点先走k步
            if not former: return   #考虑k大于链表长度的情况
            former = former.next
        while former:               #双指针共同移动：当前节点走过尾节点时后节点恰好处于倒数第k个节点
            former, latter = former.next, latter.next
        return latter

if __name__=="__main__": 
    head = listToListNode([1,2,3,4,5])
    k = 2
    printListNode(Solution().getKthFromEnd(head, k))