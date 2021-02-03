class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxCnt = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxCnt = max(maxCnt, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxCnt > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        
        return right - left

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s,k)) # 4