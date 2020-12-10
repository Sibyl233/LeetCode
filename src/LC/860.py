from typing import List
from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = Counter({5:0, 10:0, 20:0})
        for bill in bills:
            if bill == 5:
                cash[5]+=1
            elif bill == 10:
                if cash[5] == 0: 
                    return False
                cash[10]+=1
                cash[5]-=1
            elif bill == 20:
                if cash[10] >=1 and cash[5]>=1:
                    cash[10]-=1
                    cash[5]-=1
                    cash[20]+=1
                elif cash[5]>=3:
                    cash[5]-=3
                    cash[20]+=1
                else:
                    return False
        return True

if __name__ == "__main__":
    bills = [5,5,5,10,20]
    print(Solution().lemonadeChange(bills)) # True