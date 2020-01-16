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

        
if __name__ == '__main__':
    nums = [2, 7, 11, 5]
    target = 9
    print(Solution().twoSum(nums, target))