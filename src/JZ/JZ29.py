from typing import List

"""解法：模拟
- 时间复杂度：O(mn)
- 空间复杂度：O(1)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        left,right = 0, len(matrix[0])-1
        up, down = 0, len(matrix)-1
        res = []
        while True:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1
            if up > down: break
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
            if right < left: break
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            if down < up: break
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:break
        return res

"""解法：奇技淫巧
- 时间复杂度：O(?)
- 空间复杂度：O(1)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
            print(matrix)
        return res

if __name__=="__main__": 
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix)) # [1,2,3,4,8,12,11,10,9,5,6,7]