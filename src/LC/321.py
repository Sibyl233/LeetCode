from typing import List
import collections

class Solution:
    def maxNumber(self, nums1, nums2, k):
        def pickMax(nums, k):
            stack = []
            drop = len(nums) - k # 要丢掉的数字个数
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num) 
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        return max(merge(pickMax(nums1, i), pickMax(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))

if __name__ == "__main__":
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print(Solution().maxNumber(nums1, nums2, k)) # [9, 8, 6, 5, 3]