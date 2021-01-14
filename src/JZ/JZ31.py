from typing import List

"""解法：模拟。利用辅助栈模拟栈的压入、弹出操作。
- 时间复杂度：O(N)
- 空间复杂度：O(1)
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

if __name__=="__main__": 
    pushed = [1,2,3,4,5] 
    popped = [4,5,3,2,1] # [4,3,5,1,2] false
    print(Solution().validateStackSequences(pushed, popped)) # true