from typing import List

"""解法：一次遍历+贪心
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0 # 记录修改次数
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:     # 要么缩小nums[i]，要么放大nums[i+1]
                if cnt > 1:
                    return False
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1] # 缩小nums[i]，因为nums[i+1]比nums[i-1]大
                else:
                    nums[i+1] = nums[i] # 放大nums[i+1]，因为nums[i+1]太小了比nums[i-1]还小
                cnt += 1 
        return True

if __name__ == "__main__":
    nums = [3,4,2,3]
    print(Solution().checkPossibility(nums)) # false