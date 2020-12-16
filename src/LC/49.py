from typing import List
import collections

"""解法1：排序
- 时间复杂度：O(nk*logk)
- 空间复杂度：O(nk)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())

"""解法2：计数
- 时间复杂度：O(n(k+26))
- 空间复杂度：O(n(k+26))
"""
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         mp = collections.defaultdict(list)

#         for st in strs:
#             counts = [0] * 26
#             for ch in st:
#                 counts[ord(ch) - ord("a")] += 1
#             # 需将 list 转换成 tuple 才能进行哈希
#             mp[tuple(counts)].append(st)
        
#         return list(mp.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

