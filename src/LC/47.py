from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            visited = set()
            for i in range(len(nums)):
                if nums[i] in visited: 
                    continue
                visited.add(nums[i])
                backtrack(nums[:i]+nums[i+1:], path + [nums[i]])

        backtrack(nums, [])
        return res