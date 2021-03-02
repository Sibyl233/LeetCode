"""解法1：正向模拟
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""  
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        idx = 0
        arr = list(range(n))
        while len(arr) > 1:
            idx = (idx + m - 1) % len(arr)
            arr.pop(idx)
        return arr[0]

"""解法2：反推迭代
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""       
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f


if __name__ == "__main__":
    n = 10
    m = 17
    print(Solution().lastRemaining(n,m)) # 2