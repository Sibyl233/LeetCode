"""解法：模拟
- 时间复杂度：O(n)
- 空间复杂度：O(n)
"""
class Solution:
    def strToInt(self, str: str) -> int:
        res, i, sign = 0, 1, 1
        int_max, int_min, limit = 2**31-1, -2**31, 2**31//10
        
        # 1. 删除首部空格
        str = str.strip()
        if not str: return 0 # 注意此句要放在删除空格后

        # 2. 记录符号位
        if str[0] == '-':
            sign = -1
        elif str[0] != '+':
            i = 0
        
        # 3. 组合数字字符
        for c in str[i:]:
            # 遇到非数字字符跳出
            if not '0' <= c <= '9':                     
                break
            # 数字越界处理（注意是要在此轮拼接前处理）
            if res > limit or res == limit and c > '7': 
                return int_max if sign == 1 else int_min
            # 拼接数字
            res = 10 * res + ord(c) - ord('0')
        
        return sign * res

if __name__ == "__main__":
    str = "4193 with words"
    print(Solution().strToInt(str)) # 4193

