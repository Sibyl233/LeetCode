from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        import collections, functools
        lookup = collections.defaultdict(list)
        for i in range(len(ring)):
            lookup[ring[i]].append(i)

        @lru_cache(None)
        def dfs(cur, k):
            if k == len(key):
                return 0
            res = float("inf")
            for j in lookup[key[k]]:
                tmp = abs(cur - j)
                res = min(res, min(tmp, len(ring) - tmp) + 1 + dfs(j, k + 1))
            return res

        return dfs(0, 0)
        
if __name__ == "__main__":
    ring = "godding"
    key = "gd"
    print(Solution().findRotateSteps(ring, key)) # 4

