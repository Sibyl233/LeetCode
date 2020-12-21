import collections
from collections import Counter

# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:

#         # find pos - the index of the leftmost letter in our solution
#         # we create a counter and end the iteration once the suffix doesn't have each unique character
#         # pos will be the index of the smallest character we encounter before the iteration ends
#         c = Counter(s)
#         pos = 0
#         for i in range(len(s)):
#             if s[i] < s[pos]: pos = i
#             c[s[i]] -=1
#             if c[s[i]] == 0: break
#         # our answer is the leftmost letter plus the recursive call on the remainder of the string
#         # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
#         return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''

class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        seen = set() # 记录每个字母都出现
        remain_counter = collections.Counter(s) #记录每个字母出现次数

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)

if __name__ == "__main__":
    s = "cbacdcbc"
    print(Solution().removeDuplicateLetters(s)) # "acdb"