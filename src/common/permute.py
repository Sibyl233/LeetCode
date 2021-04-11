# https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/

nums = [1,2,2]
n = len(nums)
res = []


# def helper(nums,tmp,length):
#     if length == n:
#         res.append(tmp)
#     for i in range(len(nums)):
#         helper(nums[:i]+nums[i+1:],tmp+[nums[i]],length+1)

# helper(nums,[],0)
# print(res)

nums.sort()
def helper(nums,tmp,length):
    if length == n and tmp not in res:
        res.append(tmp)
    for i in range(len(nums)):
        helper(nums[:i]+nums[i+1:],tmp+[nums[i]],length+1)

helper(nums,[],0)
print(res)
