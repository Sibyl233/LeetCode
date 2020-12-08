from typing import List

"""解法：贪心
- 时间复杂度：O(nlog^2*C)。n位字符串长度，C位题目规定的整数范围。
- 空间复杂度：O(n)
"""
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []

        def backtrack(idx: int):
            if idx == len(S):
                return len(ans) >= 3
            
            cur = 0
            for i in range(idx, len(S)):
                
                if i > idx and S[idx] == "0":  
                    break # 剪枝1：拆分出的数以0开头
                cur = cur * 10 + ord(S[i]) - ord("0")
                if cur > 2**31 - 1:           
                    break # 剪枝2：拆分出的数超过题设范围
                
                if len(ans) < 2 or cur == ans[-2] + ans[-1]:
                    ans.append(cur)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and cur > ans[-2] + ans[-1]:
                    break # 剪枝3：拆分出的数大于最后两数之和
        
            return False
        
        backtrack(0)
        return ans

if __name__ == "__main__":
    S = "123456579"
    print(Solution().splitIntoFibonacci(S)) # [123,456,579]
