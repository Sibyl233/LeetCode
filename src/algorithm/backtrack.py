'''
模板
'''
# res = []
# def backpath(路径，选择列表):
#     if 满足结束条件:
#         res.append(路径)
#         return
#     for 选择 in 选择列表:
#         if 选择 不满足合法条件:
#             continue # 剪枝
#         做选择
#         backpath(新路径，新选择列表)
#         撤销选择

'''
全排列（详解）
'''
# V0: 完全套用模板
# def permute(nums):
#     def backtrack(path, nums):
#         if len(path) == len(nums):
#             res.append(path.copy())
#             return
#         for i in range(len(nums)):
#             if (nums[i] in path):
#                 continue
#             path.append(nums[i])
#             backtrack(path,nums)
#             path.pop()
    
#     res = []
#     backtrack([], nums)
#     return res

# V1: 将路径作为参数传递到下一层递归
# def permute(nums):
#     def backtrack(path, nums):
#         if len(path) == len(nums):
#             res.append(path)
#             return
#         for i in range(len(nums)):
#             if (nums[i] in path):
#                 continue
#             backtrack(path + [nums[i]], nums)
    
#     res = []
#     backtrack([], nums)
#     return res

# V2: 将选择列表作为参数传递到下一层递归
# def permute(nums):
#     def backtrack(path, nums):
#         if not nums:
#             res.append(path)
#             return
#         for i in range(len(nums)):
#             backtrack(path + [nums[i]], nums[:i]+nums[i+1:])
    
#     res = []
#     backtrack([], nums)
#     return res

# V3: 含重复元素
def permute(nums):
    def backtrack(path, nums):
        if not nums and path not in res: # 在加入res列表时判断该排列是否在列表中存在即可
            res.append(path)
            return
        for i in range(len(nums)):
            backtrack(path + [nums[i]], nums[:i]+nums[i+1:])
    
    res = []
    backtrack([], nums)
    return res

'''
组合
'''
def combination(nums,target):
    nums.sort()
    n = len(nums)
    def backtrack(path, pathSum, idx):
        if pathSum == target:
            res.append(path)
            return
        for i in range(idx,n):
            if pathSum + nums[idx] > target:
                break
            if i>idx and nums[i]==nums[i-1]:
                continue
            backtrack(path+[nums[i]], pathSum+nums[i], i+1)
    
    res = []
    backtrack([], 0, 0)
    return res

'''
子集
'''
def subset(nums):
    nums.sort()
    n = len(nums)
    def helper(path, idx):
        if path not in res:
            res.append(path)
            # return 注意这里不需要返回
        for i in range(idx,n):
            helper(path+[nums[i]], i+1)
  
    res = []
    helper([],0)
    return res



if __name__ == '__main__':
    nums1 = [1,2,2]
    nums2 = [10,1,2,7,6,1,5]
    target = 8
    print(permute(nums1))
    print(combination(nums2,target))
    print(subset(nums1))