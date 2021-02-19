from typing import List
import collections

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        queue = collections.deque()
        res = 0
        for i in range(N):
            if queue and queue[0] + K <= i:
                queue.popleft()
            if len(queue) % 2 == A[i]:
                if i + K > N: return -1
                queue.append(i)
                res += 1
        return res

if __name__ == "__main__":
    A = [0,0,0,1,0,1,1,0]
    K = 3
    print(Solution().minKBitFlips(A,K)) # 3