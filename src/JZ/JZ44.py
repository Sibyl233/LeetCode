"""解法：找规律
- 时间复杂度：O(logn)
- 空间复杂度：O(logn)
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        # 第一步：确定位数 digit
        while n > count: 
            n -= count
            start *= 10 # 1,10,100...
            digit += 1  # 1,2,3...
            count = 9 * start * digit # 9,180,2700
        # 第二步：确定数字 num
        num = start + (n - 1) // digit 
        # 第三步：确定数字中的数位
        return int(str(num)[(n - 1) % digit]) 

if __name__ == "__main__":
    n = 11
    print(Solution().findNthDigit(n)) # 0