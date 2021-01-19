from typing import List
import collections

"""解法：并查集
- 时间复杂度：O(nα(n))。其中 α 为 Ackermann 函数的反函数。
- 空间复杂度：O(n)
"""
class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))
    
    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
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
        # print(emailToIndex)
        # print(emailToName)
        
        dsu = DisjointSetUnion(len(emailToIndex))
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                dsu.unionSet(firstIndex, emailToIndex[email])
        
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = dsu.find(index)
            indexToEmails[index].append(email)
        # print(indexToEmails)
        
        ans = list()
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

