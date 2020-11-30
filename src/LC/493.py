from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        def merge(nums, start, mid, end, temp):
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <=  nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            # 防住
            # 这里代码开始
            ti, tj = start, mid + 1
            while ti <= mid and tj <= end:
                if nums[ti] <=  2 * nums[tj]:
                    ti += 1
                else:
                    self.cnt += mid - ti + 1
                    tj += 1
            # 这里代码结束
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            for i in range(len(temp)):
                nums[start + i] = temp[i]
            temp.clear()
                    

        def mergeSort(nums, start, end, temp):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid, temp)
            mergeSort(nums, mid + 1, end, temp)
            merge(nums, start, mid,  end, temp)
        mergeSort(nums, 0, len(nums) - 1, [])
        return self.cnt

if __name__ == "__main__":
    nums = [1,3,2,3,1]
    print(Solution().reversePairs(nums)) # 2