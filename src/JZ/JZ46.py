"""解法：递归
- 时间复杂度：O(logn)
- 空间复杂度：O(logn)
"""
class Solution:
    def translateNum(self, num: int) -> int:
        if num <= 9:
            return 1
        ba = num % 100 # 从后往前末两位
        if 10 <= ba <= 25:
            return self.translateNum(num//10) + self.translateNum(num//100)
        return self.translateNum(num//10)
            
if __name__ == "__main__":
    num = 12258
    print(Solution().translateNum(num)) # 5