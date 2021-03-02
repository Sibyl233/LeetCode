from typing import List

"""解法1：遍历 + 集合
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""  
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        minNum, maxNum = 14, 0 # 注意
        repeat = set()
        for num in nums:
            if num == 0: continue
            if num in repeat: return False
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)
            repeat.add(num)
        return maxNum - minNum < 5

"""解法2：排序
- 时间复杂度：O(nlogn)
- 空间复杂度：O(1)
"""  
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

if __name__ == "__main__":
    nums = [0,0,1,2,5]
    print(Solution().isStraight(nums)) # True