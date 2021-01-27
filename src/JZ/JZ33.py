"""解法1：递归
- 时间复杂度：O(N^2)。每次调用递归减去一个根节点，因此递归占用O(N)；最差情况下（即当树退化为链表），每轮递归都需遍历树所有节点，占用O(N)。
- 空间复杂度：O(N)。最差情况下（即当树退化为链表），递归深度将达到 N 。
"""
# class Solution:
#     def verifyPostorder(self, postorder: [int]) -> bool:
#         def verify(postorder, l, r):
#             # 边界判断
#             if l >= r: 
#                 return True
#             # 找到左右子树划分点（同时已经判断了左子树）
#             mid = l
#             while postorder[mid] < postorder[r]: 
#                 mid += 1
#             # 判断右子树
#             tmp = mid+1
#             while tmp < r: 
#                 if postorder[tmp] < postorder[r]:
#                     return False
#                 else:
#                     tmp += 1
#             # 递归左右子树
#             return verify(postorder, l, mid - 1) and verify(postorder, mid, r - 1)

#         return verify(postorder, 0, len(postorder) - 1)

"""解法2：栈。不好理解。
- 时间复杂度：O(N)。遍历 postorder 所有节点，各节点均入栈 / 出栈一次，使用O(N)时间。
- 空间复杂度：O(N)。最差情况下，单调栈 stack 存储所有节点，使用 O(N) 额外空间。
"""
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1): # 注意这里是倒序遍历
            if postorder[i] > root: 
                return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True

if __name__=="__main__": 
    postorder = [1,6,3,2,5]
    print(Solution().verifyPostorder(postorder)) # False