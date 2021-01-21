''' 栈 '''
# 使用列表实现
stack = []

# 入栈和出栈
stack.append(1) # 元素 1 入栈
stack.append(2) # 元素 2 入栈
stack.pop()     # 元素 2 出栈
stack.pop()     # 元素 1 出栈



''' 队列 '''
# 使用双端队列 collections.deque 实现
from collections import deque
queue = deque()

# 入队和出队
queue.append(1) # 元素 1 入队
queue.append(2) # 元素 2 入队
queue.popleft() # 元素 1 出队
queue.popleft() # 元素 2 出队






