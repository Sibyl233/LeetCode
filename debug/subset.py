nums = [1,2,2]
n = len(nums)
res = []

# nums中元素不重复
# [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
# def helper(idx,tmp):
#     res.append(tmp)
#     for i in range(idx,n):
#         helper(i+1,tmp+[nums[i]])
# helper(0,[])
# print(res)

# nums中有元素重复
nums.sort() # 需要先排序
def helper(idx,tmp):
    if tmp not in res:
        res.append(tmp)
    for i in range(idx,n):
        helper(i+1,tmp+[nums[i]])
helper(0,[])
print(res)