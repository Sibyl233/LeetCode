from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if nums[i]>0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            p,q = i+1,n-1
            while p < q:
                if nums[p] + nums[q] == target:
                    res.append([nums[i],nums[p],nums[q]])
                    while p<q and nums[p]==nums[p+1]:
                        p += 1
                    while p<q and nums[q]==nums[q-1]:
                        q -= 1
                    p += 1
                    q -= 1
                elif nums[p] + nums[q] < target:
                    p += 1
                else:
                    q -= 1
        return res