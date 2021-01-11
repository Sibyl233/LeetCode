from typing import List

"""解法：一次遍历
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if len(nums)==0: return res

        # 末尾添加一个不连续的数
        nums.append(nums[0]-1)
        
        start=end=nums[0]
        for i in range(1, len(nums)):
            if nums[i]-1 == nums[i-1]:
                end = nums[i]
            else:
                if start==end:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
                start=end=nums[i]
        return res

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    print(Solution().summaryRanges(nums)) # ["0->2","4->5","7"]