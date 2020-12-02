from typing import List

"""需满足两个条件：1）总加油量>=总耗油量；2）任意时刻油箱剩余量>=0
- 时间复杂度：O(N)
- 空间复杂度：O(1)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, cur, res = 0, 0, 0           # total记录总油量-总油耗，cur记录当前油量，res记录出发位置
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:                     
                cur = 0                     # 在新位置重新开始计算油耗情况
                res = i + 1                 # 将起始位置改成i+1
        return res if total >= 0 else -1    

if __name__ == '__main__':
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(Solution().canCompleteCircuit(gas,cost)) # 3

