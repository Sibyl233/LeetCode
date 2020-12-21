class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         return list(Counter(t) - Counter(s))[0]

if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t)) # "e"