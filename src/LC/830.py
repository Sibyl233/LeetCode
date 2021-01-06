from typing import List

"""解法：一次遍历
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        n, num = len(s), 1

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if num >= 3:
                    res.append([i - num + 1, i])
                num = 1
            else:
                num += 1
        
        return res

if __name__ == "__main__":
    s = "abcdddeeeeaabbbcd"
    print(Solution().largeGroupPositions(s)) # [[3,5],[6,9],[12,14]]
