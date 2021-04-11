class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        return "".join(stack)

if __name__=="__main__": 
    S = "abbaca"
    print(Solution().removeDuplicates(S)) # "ca"