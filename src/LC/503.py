from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(n * 2):
            while stack and nums[i % n] > nums[stack[-1]]  :
                res[stack.pop()] = nums[i % n]
            stack.append(i % n) # 栈里面需要保存元素在数组中的下标，而不是具体的数字。因为需要根据下标修改结果数组 res
        return res

if __name__ == "__main__":
    nums = [1,2,1]
    print(Solution().nextGreaterElements(nums))# [2,-1,2]