from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'),x))

if __name__ == "__main__":
    arr = [2,3,5,7,11,13,17,19]
    print(Solution().sortByBits(arr)) # [2,3,5,17,7,11,13,19]