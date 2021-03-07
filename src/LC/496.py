from typing import List

"""解法1_1：暴力。遍历nums1，找到元素在nums2中的位置，再找它之后比它大的。
- 时间复杂度：O(n^2)
- 空间复杂度：O(1)
"""
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = []
#         for num1 in nums1:
#             flag = 0
#             bigger = -1
#             for num2 in nums2:
#                 if num1 == num2:
#                     flag = 1
#                 if flag == 1 and num1 < num2:
#                     bigger = num2 
#                     break
#             res.append(bigger)
#         return res

"""解法1_2：暴力+哈希表。先处理nums2，再用哈希表和nums1建立联系。
- 时间复杂度：O(n^2)
- 空间复杂度：O(n)
"""
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         dic = {}

#         for i in range(len(nums2)):
#             for j in range(i+1,len(nums2)):
#                 if nums2[j] > nums2[i]:
#                     dic[nums2[i]] = nums2[j]
#                     break
                    
#         return [dic.get(num1,-1) for num1 in nums1]

"""解法2：单调栈 + 哈希表。
- 时间复杂度：O(m+n)
- 空间复杂度：O(n)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = [], {}
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                dic[stack.pop()] = num2
            stack.append(num2)
        return [dic.get(num1,-1) for num1 in nums1]


if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution().nextGreaterElement(nums1,nums2)) # [-1,3,-1]