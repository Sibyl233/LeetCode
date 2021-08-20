'''
最长上升子序列 Longest Increasing Subsequence
'''

# 最长上升子序列长度
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j]+1, dp[i])
    return max(dp)

# 最长上升子序列个数
def numberOfLIS(nums):
    n = len(nums)
    length = [1] * n
    count = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if length[j]+1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j]+1 == length[i]:
                    count[i] += count[j] 
    maxLength = max(length)
    return sum(count[i] for i in range(n) if length[i] == maxLength)

if __name__ == "__main__":
    nums = [1,3,5,4,7]
    print(lengthOfLIS(nums))
    print(numberOfLIS(nums))