class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hashmap: 
                return [hashmap[dif], i]
            hashmap[n] = i
        return []