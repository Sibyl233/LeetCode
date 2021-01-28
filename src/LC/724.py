from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = [0]
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            preSum.append(tmp)
        for j in range(len(nums)):
            if preSum[j] == preSum[-1]-preSum[j+1]:
                return j
        return -1

if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    print(Solution().pivotIndex(nums)) # 3