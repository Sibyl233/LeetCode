from typing import List
import collections

"""解法：并查集
- 时间复杂度：O(nα(n))。其中 α 为 Ackermann 函数的反函数。
- 空间复杂度：O(n)
"""
class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n      # 初始化子树的大小为1
        self.pa = list(range(n)) # 记录某个人的父母是谁
    
    def find(self, x: int) -> int:
        if x != self.pa[x]:                    # x不是自身的父母，即x不是该集合的代表
            self.pa[x] = self.find(self.pa[x]) # 查找x的祖先直到找到代表,
        return self.pa[x]                      # 顺带路径压缩
    
    def unionSet(self, x: int, y: int) -> bool:
        xx, yy = self.find(x), self.find(y)
        
        if xx == yy:
            return False
        
        if self.rank[xx] > self.rank[yy]: # 保证小的合到大的
            xx, yy = yy, xx
        
        self.pa[xx] = yy
        self.rank[yy] += self.rank[xx]
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name
        print(emailToIndex)
        print(emailToName)
        
        dsu = DisjointSetUnion(len(emailToIndex))
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                dsu.unionSet(firstIndex, emailToIndex[email])
        
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = dsu.find(index)
            indexToEmails[index].append(email)
        print(indexToEmails)
        
        ans = []
        for emails in indexToEmails.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
        return ans

if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
                ["John", "johnnybravo@mail.com"], 
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
                ["Mary", "mary@mail.com"]]
    print(Solution().accountsMerge(accounts)) 
    # [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], 
    #  ["John", "johnnybravo@mail.com"], 
    #  ["Mary", "mary@mail.com"]]

