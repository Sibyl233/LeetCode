from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        pre,cnt = 0,0
        for num in nums:
            pre += num
            if pre == k:
                cnt += 1
            if pre - k in d:
                cnt += d[pre-k]
            if pre in d:
                d[pre] += 1
            else:
                d[pre] = 1
        return cnt