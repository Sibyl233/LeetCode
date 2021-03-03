import collections

"""解法1：BFS
- 时间复杂度：O(mn)
- 空间复杂度：O(mn)
"""
# class Solution:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         visited = set()
#         queue = collections.deque()
#         queue.append((0,0))
#         while queue:
#             (x,y) = queue.popleft()
#             if (x,y) not in visited and x<m and y<n and self.digitSum(x)+self.digitSum(y) <= k:
#                 visited.add((x,y))
#                 queue.append((x+1,y))
#                 queue.append((x,y+1))
#         return len(visited)
    
#     def digitSum(self, num):
#         ans = 0
#         while num:
#             ans += num % 10
#             num //= 10
#         return ans

"""解法2：DFS
- 时间复杂度：O(mn)
- 空间复杂度：O(mn)
"""
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        def dfs(x,y):
            if (x,y) not in visited and x<m and y<n and self.digitSum(x)+self.digitSum(y) <= k:
                visited.add((x,y))
                dfs(x+1,y)
                dfs(x,y+1) 
        dfs(0,0)
        return len(visited)
    
    def digitSum(self, num):
        ans = 0
        while num:
            ans += num % 10
            num //= 10
        return ans

if __name__=="__main__": 
    m = 2
    n = 3
    k = 1
    print(Solution().movingCount(m,n,k)) # True