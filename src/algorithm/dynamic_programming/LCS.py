'''
最长公共子序列 Longest Common Subsequence
最长重复子数组 Longest Repeated Subarray
'''

# 最长公共子序列（不一定连续）
def lengthOfLCS(text1, text2):
        m = len(text1)
        n = len(text2)
        res = 0
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    res = max(res,dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return res

# 最长重复子数组（连续）
def lengthOfLRS(A, B):
        m = len(A)
        n = len(B)
        res = 0
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    res = max(res, dp[i][j])
        
        return res

if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace" 
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    print(lengthOfLCS(text1,text2))
    print(lengthOfLRS(A,B))