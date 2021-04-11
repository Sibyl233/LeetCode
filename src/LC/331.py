class Solution(object):
    def isValidSerialization(self, preorder):
        stack = []
        for node in preorder.split(','):
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop(), stack.pop(), stack.pop()
                stack.append('#')
        return len(stack) == 1 and stack.pop() == '#'

if __name__ == "__main__":
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    print(Solution().isValidSerialization(preorder))