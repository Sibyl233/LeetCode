# nums = [2,3,5]
nums = [10,1,2,7,6,1,5]
target = 8
n = len(nums)
res = []

# nums.sort()
# def helper(idx,tmpSum,tmp):
#     if tmpSum == target:
#         res.append(tmp)
#         return
#     # if tmpSum > target or idx==n:
#     #     return
#     for i in range(idx,n):
#         if tmpSum + nums[i] > target:
#             break
#         helper(i, tmpSum + nums[i],tmp+[nums[i]])
    
# helper(0,0,[])
# print(res)

nums.sort()
def helper(idx,tmpSum,tmp):
    if tmpSum == target:
        res.append(tmp)
        return
    # if tmpSum > target or idx==n:
    #     return
    for i in range(idx,n):
        if tmpSum + nums[i] > target:
            break
        if i>idx and nums[i]==nums[i-1]:
            continue
        helper(i+1, tmpSum + nums[i],tmp+[nums[i]])
    
helper(0,0,[])
print(res)
