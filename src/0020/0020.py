class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in hashmap:
                top_element = stack.pop() if stack else '#'
                if hashmap[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == '__main__':
    s = '([)]'
    print(Solution().isValid(s))