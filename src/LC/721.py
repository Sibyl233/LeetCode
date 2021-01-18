from typing import List
import collections

class Node:
    def __init__(self, data):
        self.data = data

def makeSet(x):
    """
    make x as a set.
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    x.parent = x

def unionSet(x, y):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = findSet(x), findSet(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def findSet(x):
    """
    return the parent of x
    """
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent

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

        vertex = [ Node(i) for i in range(len(emailToIndex)) ]
        for v in vertex:
            makeSet(v)
        
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                unionSet(vertex[firstIndex], vertex[emailToIndex[email]])
        
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = findSet(vertex[index])
            indexToEmails[index].append(email)
        # print(indexToEmails)
        
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

