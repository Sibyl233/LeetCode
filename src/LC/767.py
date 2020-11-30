import collections

class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S
        
        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""
        
        reorganizeArray = [""] * length
        evenIndex, oddIndex = 0, 1
        halfLength = length // 2

        for c, count in counts.items():
            while count > 0 and count <= halfLength and oddIndex < length:
                reorganizeArray[oddIndex] = c
                count -= 1
                oddIndex += 2
            while count > 0:
                reorganizeArray[evenIndex] = c
                count -= 1
                evenIndex += 2
        
        return "".join(reorganizeArray)

if __name__ == "__main__":
    S = "aaab"
    print(Solution().reorganizeString(S)) # ""