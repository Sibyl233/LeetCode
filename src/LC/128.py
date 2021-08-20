class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        res = 0
        for num in nums:
            if num not in dic:
                left = dic.get(num-1,0)
                right = dic.get(num+1,0)

                curLength = 1+left+right
                res = max(res,curLength)

                dic[num] = curLength
                dic[num-left] = curLength
                dic[num+right] = curLength
        
        return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return n
        nums.sort()
        length, res = 1,1
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                continue
            if nums[i]-nums[i-1] ==1  :
                length += 1
                res = max(res,length)
            else:
                length = 1
        return res