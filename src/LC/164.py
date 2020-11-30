from typing import List

"""
解法1：基数排序
    - 时间复杂度：O(n)
    - 空间复杂度：O(n)
"""
# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         if len(nums) < 2:
#             return 0
        
#         # 基数排序
#         RADIX = 10
#         placement = 1
#         maxDigit = max(nums)
#         while placement <= maxDigit:
#             buckets = [[] for _ in range(RADIX)]
#             for i in nums:
#                 tmp = int((i / placement) % RADIX)
#                 buckets[tmp].append(i)
#             a = 0
#             for b in range(RADIX):
#                 for i in buckets[b]:
#                     nums[a] = i
#                     a += 1
#             placement *= RADIX
        
#         return max((nums[i+1]-nums[i]) for i in range(len(nums)-1))

"""
解法2：桶排序
    - 时间复杂度：O(n)
    - 空间复杂度：O(n)
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int: 
        if len(nums) < 2:
            return 0
        
        maxNum = max(nums)
        minNum = min(nums)
        maxGap = 0
        bucketLen = max(1,(maxNum-minNum)//(len(nums)-1))            # 桶长
        buckets = [[]for _ in range((maxNum-minNum)//bucketLen + 1)] # 桶数

        for i in range(len(nums)):
            pos = (nums[i]-minNum) // bucketLen
            buckets[pos].append(nums[i])

        preMax = float('inf')
        for i in range(len(buckets)):
            if buckets[i] and preMax != float('inf'):
                maxGap = max(maxGap, min(buckets[i])-preMax)
            if buckets[i]:
                preMax = max(buckets[i])
        return maxGap

if __name__ == "__main__":
    nums = [3,6,9,1]
    print(Solution().maximumGap(nums))