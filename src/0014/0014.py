class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, word in enumerate(zip(*strs)):
            if len(set(word)) > 1:
                return strs[0][:i]
        else:
            return min(strs) 


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))