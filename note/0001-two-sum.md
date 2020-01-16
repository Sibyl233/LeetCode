#### 0001-两数之和

直观思路：每次判断`target-num[i]`对应的值是否在`num[i+1:]`中。但考虑到查找索引的最差情况，修改成每次从`nums[:i]`中去查找是否有`target - nums[i]`。

```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            dif = target - n
            if dif in nums[:i]:
                return [nums.index(dif), i]
        return []
```

采用更加合适的字典数据结构：

```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hashmap: 
                return [hashmap[dif], i]
            hashmap[n] = i
        return []
```

