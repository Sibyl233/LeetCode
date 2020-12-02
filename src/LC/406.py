from typing import List

"""解法：排序+遍历
- 时间复杂度：O(n^2)
- 空间复杂度：O(log(n))
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按h降序，再按k升序
        people.sort(key=lambda x: (-x[0], x[1])) 
        ans = []
        for person in people:
            ans[person[1]:person[1]] = [person]
            # ans.insert(person[1], person)
        return ans

if __name__ == "__main__":
    people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(Solution().reconstructQueue(people)) # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]