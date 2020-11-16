class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k # 处理数字还没删除完的情况（比如数字序列单调递增）
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0' # 删去前导零

if __name__ == "__main__":
    num = "1432219"
    k = 3
    print(Solution().removeKdigits(num,k)) # 1219