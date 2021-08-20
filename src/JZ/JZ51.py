from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.mergeSort(nums)
        return self.cnt
    
    def mergeSort(self,nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        # 分
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        # 合并
        return self._merge(left, right)

    def _merge(self, left, right):
        res = [] # 辅助空间
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                self.cnt += len(left)-i
                j += 1
        res += left[i:]
        res += right[j:]
        return res