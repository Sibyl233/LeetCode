import collections
import heapq

"""
解法1：基于堆的贪心算法
- 时间复杂度：O(nlog∣Σ∣+∣Σ∣)
- 空间复杂度：O(∣Σ∣)
"""
# class Solution:
#     def reorganizeString(self, S: str) -> str:
#         # 边界处理
#         length = len(S)
#         counts = collections.Counter(S)
#         maxCount = max(counts.items(), key=lambda x: x[1])[1]
#         if length < 2:
#             return S
#         if maxCount > (length + 1) // 2:
#             return ""
        
#         # 放置字符
#         queue, res = [], ""
#         pre = (0,None) # 表示前一次被放置的字符
#         for c,count in counts.items():
#             heapq.heappush(queue,(-count,c)) # 构造堆
#         while queue:
#             count, c = heapq.heappop(queue)  # 弹出堆顶元素
#             res += c
#             if pre[0] < 0:
#                 heapq.heappush(queue,pre)    # 更新堆
#             pre = (count+1,c)

#         return res

"""
解法2：基于计数的贪心算法
- 时间复杂度：O(n+∣Σ∣)
- 空间复杂度：O(∣Σ∣)
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        # 边界处理
        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if length < 2:
            return S
        if maxCount > (length + 1) // 2:
            return ""

        # 放置字符        
        reorganizeArray = [""] * length
        evenIndex, oddIndex = 0, 1
        for c, count in counts.items():
            while count > 0 and count < (length + 1) // 2 and oddIndex < length:
                reorganizeArray[oddIndex] = c
                count -= 1
                oddIndex += 2
            while count > 0:
                reorganizeArray[evenIndex] = c
                count -= 1
                evenIndex += 2
        
        return "".join(reorganizeArray)

if __name__ == "__main__":
    S = "aaab"
    print(Solution().reorganizeString(S)) # ""