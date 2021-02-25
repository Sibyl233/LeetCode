from typing import List

"""解法：滑动窗口
- 时间复杂度：O(n)。需要对两个数组各遍历两次
- 空间复杂度：O(1)
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)  
        ans = sum([customers[i] for i in range(N) if grumpy[i] == 0 or i < X]) # 所有不生气时间内的顾客总数
        cur = sum([customers[i] * grumpy[i] for i in range(X)]) # 初始化cur，cur表示生气的X分钟内会让多少顾客不满意
        res = cur

        for i in range(X, N):         
            # if grumpy[i] == 1:     # 如果新进入窗口的元素是生气的，累加不满意的顾客数到滑动窗口中
            #     cur += customers[i]
            # if grumpy[i - X] == 1: # 如果离开窗口的元素是生气的，从滑动窗口中减去该不满意的顾客数
            #     cur -= customers[i - X]
            cur = cur + customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            res = max(res, cur)
        return ans + res

if __name__ == "__main__":
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    X = 3
    print(Solution().maxSatisfied(customers, grumpy, X)) # 16
