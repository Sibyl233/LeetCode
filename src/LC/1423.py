from typing import List

"""解法：滑动窗口
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        windowSize = n - k                        # 滑动窗口大小为 n-k
        tmp = minSum = sum(cardPoints[:windowSize]) # 选前 n-k 个的和作为初始值
        for i in range(windowSize, n):
            # 滑动窗口每向右移动一格，增加从右侧进入窗口的元素值，并减少从左侧离开窗口的元素值
            tmp += cardPoints[i] - cardPoints[i - windowSize]
            minSum = min(minSum, tmp)
        return sum(cardPoints) - minSum

if __name__ == "__main__":
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(Solution().maxScore(cardPoints, k)) # 12
