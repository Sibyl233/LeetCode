from typing import List
import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect.bisect_right(pre, now - lower) - bisect.bisect_left(pre, now - upper)
            bisect.insort(pre, now)
        return res

if __name__ == "__main__":
    nums, lower, upper = [-2,5,1], -2, 2
    print(Solution().countRangeSum(nums, lower, upper)) # 2