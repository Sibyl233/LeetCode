from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque,res = [],[] # deque也可以用collection里的双端队列实现
        for i in range(0, len(nums)):
            while deque and nums[i]>nums[deque[-1]]: # 只存有可能成为最大值的数字的index进deque
                deque.pop()
            deque.append(i)
            while i-deque[0]>k-1: # 是否还处于滑动窗口中
                deque.pop(0)
            if i >= k-1:
                res.append(nums[deque[0]])
        return res

if __name__=="__main__": 
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k)) # [3,3,5,5,6,7] 
