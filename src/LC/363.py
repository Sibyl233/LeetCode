from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        r, c = len(matrix),len(matrix[0])
        res = float('-inf') 
        for upper in range(r):
            rowSum = [0] * c
            for lower in range(upper, r):
                for i in range(c):
                    rowSum[i] += matrix[lower][i]

                res = max(res, self.maxSubArray(rowSum,k))
        return res
        
    def maxSubArray(self, nums: List[int], k:int) -> int:
        # 最大数组和
        maxSum = res = nums[0]
        for i in range(1,len(nums)):
            maxSum = max(maxSum+nums[i], nums[i])
            res = max(maxSum,res)
        if res<=k: return res
        
        # 小于 k 的最大数组和
        res = float('-inf')
        for i in range(len(nums)):
            maxSum = 0
            for j in range(i,len(nums)):
                maxSum += nums[j]
                if res<maxSum<=k:
                    res = maxSum
                if res == k:
                    return k
        return res
    
if __name__ == "__main__":
    matrix = [[2,2,-1]]
    k = 0
    # matrix = [[1,0,1],[0,-2,3]]
    # k = 2
    print(Solution().maxSumSubmatrix(matrix,k)) # -1