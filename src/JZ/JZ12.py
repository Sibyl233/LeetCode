from typing import List

"""解法1：DFS + 剪枝
- 时间复杂度：O(3^K*MN)
- 空间复杂度：O(K)
"""
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def dfs(i, j, k):
#             if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: 
#                 return False
#             if k == len(word) - 1: 
#                 return True
#             board[i][j] = ''
#             res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
#             board[i][j] = word[k]
#             return res

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(i, j, 0): 
#                     return True
#         return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i: int, j: int, k: int) -> bool:
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            #res = False
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            visited.remove((i, j))
            return res

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False

if __name__=="__main__": 
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCEE"
    print(Solution().exist(board, word)) # True     