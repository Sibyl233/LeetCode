from typing import List

"""解法：二元组表示+计数
- 时间复杂度：O(n)。n是多米诺骨牌数量。
- 空间复杂度：O(1)
"""
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        res = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            res += num[val]
            num[val] += 1
        return res

if __name__ == "__main__":
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    print(Solution().numEquivDominoPairs(dominoes)) # 1