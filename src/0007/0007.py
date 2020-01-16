class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = int(str(abs(x))[::-1])
        if res > pow(2, 31):
            res = 0
        return -res if x < 0 else res

if __name__ == '__main__':
    x = -123
    print(Solution().reverse(x))