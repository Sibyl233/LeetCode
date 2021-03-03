class Solution:
    def sumNums(self, n: int) -> int:
        # and两侧如果是数值变量则用于判断是否非0，如果非0则返回后一个数,否则返回0
        return n and (n + self.sumNums(n-1))           

if __name__ == "__main__":
    n = 9
    print(Solution().sumNums(n)) # 45