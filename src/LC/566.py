from typing import List

"""解法：二维数组的一维表示
- 时间复杂度：O(rc)
- 空间复杂度：O(1)
"""
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        
        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = nums[x // n][x % n] # 将x映射为矩阵下标
        
        return ans

if __name__ == "__main__":
    nums = [[1,2],
            [3,4]]
    r = 1
    c = 4
    print(Solution().matrixReshape(nums,r,c)) # [[1,2,3,4]]