from typing import List

"""解法：动态规划
- 时间复杂度：O(mn)
- 空间复杂度：O(1)
"""
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: 
                    continue
                if i == 0: 
                    grid[i][j] += grid[i][j - 1]
                elif j == 0: 
                    grid[i][j] += grid[i - 1][j]
                else: 
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]

if __name__ == "__main__":
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    print(Solution().maxValue(grid)) # 12 (1→3→5→2→1)