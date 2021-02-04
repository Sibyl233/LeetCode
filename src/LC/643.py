from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = tmp = sum(nums[:k])
        n = len(nums)
        # 滑动窗口
        for i in range(k,n):
            tmp = tmp + nums[i] - nums[i-k]
            res = max(res,tmp)
        return res / k

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(Solution().findMaxAverage(nums,k)) # 12.75