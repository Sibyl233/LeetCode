import heapq
import collections

"""解法1：堆
- 时间复杂度：O(min(R,D)logmax(R,D))
- 空间复杂度：O(R+D)
"""
# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         hd = [i for i, s in enumerate(senate) if s == "D"]
#         hr = [i for i, s in enumerate(senate) if s == "R"]

#         while hr and hd:
#             if hr[0] < hd[0]:
#                 heapq.heappop(hd)
#                 heapq.heappush(hr, heapq.heappop(hr) + len(senate))
#             else:
#                 heapq.heappop(hr)
#                 heapq.heappush(hd, heapq.heappop(hd) + len(senate))
#         return "Dire" if not hr else "Radiant"

"""解法2：双端队列
- 时间复杂度：O(min(R,D))
- 空间复杂度：O(R+D)
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qd = collections.deque([i for i, s in enumerate(senate) if s == "D"])
        qr = collections.deque([i for i, s in enumerate(senate) if s == "R"])

        while qr and qd:
            if qr[0] < qd[0]:
                qd.popleft()
                qr.append(qr.popleft() + len(senate)) # 增加固定的len(senate)表示进入下一轮投票
            else:
                qr.popleft()
                qd.append(qd.popleft() + len(senate))
        return "Dire" if not qr else "Radiant"

if __name__ == "__main__":
    senate = "RDD"
    print(Solution().predictPartyVictory(senate)) # "Dire"
