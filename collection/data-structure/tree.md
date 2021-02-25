## 树

### 定义

在单链表中，每个节点仅有一个后继节点，当节点有**多个后继节点**，但**只有一个前驱节点**的时候，就变成了一棵「树」。

### 概念

- 树的节点类型：根节点、中间节点、叶节点。
- 树的节点关系：父子关系、兄弟关系、祖孙关系
- 常用定义：子树、节点深度、节点距离
- 树的类型：**二叉树**、多叉树
  - 满二叉树
  - 完全二叉树
  - 二叉搜索树

### 表示

以二叉树为例，每个节点包含三个成员变量：值 `val`、左子节点 `left`、右子节点 `right` 。

```python
# 定义
class TreeNode:
    def __init__(self, x):
        self.val = x      # 节点值
        self.left = None  # 左子节点
        self.right = None # 右子节点
```

构建一棵如下二叉树

```
    3
   / \
  4   5
 / \
1   2
```

```python
# 初始化节点
n1 = TreeNode(3) 
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(1)
n5 = TreeNode(2)

# 构建引用指向
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
```

### 操作

#### 前/中/后序遍历

这三种遍历方式都是**深度优先**的（总是从根节点先走到底，然后再回溯），因此实现上采用 DFS。

- 前序遍历：根 → 左子树 → 右子树
- 中序遍历：左子树 → 根 → 右子树
- 后序遍历：左子树 → 右子树 → 根

以实现前序遍历的代码为例：前面部分是到达叶子节点为条件的递归出口；在非叶子节点上，只需先访问当前节点，然后依次递归他的左右孩子就可以了。中序和后序遍历的代码同理，由于只有根节点的访问时机不同，只需修改根节点的访问顺序就可以了。

> Tip：在树相关的题目中多用递归来实现某些逻辑，而递归的出口条件往往是到达叶节点的时候。

```python
def preOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if not node: 
            return node
        # 前序遍历
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    res = []
    dfs(root)
    return res

def inOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if not node: 
            return node
        # 中序遍历
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    
    res = []
    dfs(root)
    return res

def postOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if not node: 
            return node
        # 后序遍历
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    
    res = []
    dfs(root)
    return res
```

#### 层次遍历

层次遍历是一个**广度优先**的遍历过程，所以在实现上需要将 DFS 替换为 BFS 。

```python
import collections
def levelOrder(root: TreeNode) -> List[int]:
    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return res

# 逐层打印 V1
def levelOrder(root: TreeNode) -> List[List[int]]:
    res = [], 
    queue = collections.deque()
    queue.append(root)
    while queue:
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(tmp)
    return res
  
# 逐层打印 V2
def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    queue = collections.deque()
    queue.append((root,0))
    while queue:
        node, depth = queue.popleft()
        if depth == len(res):
            res.append([])
        res[depth].append(node.val)
        if node.left: queue.append((node.left, depth+1))
        if node.right: queue.append((node.right, depth+1))
    return res
```



### 参考

1. https://leetcode-cn.com/leetbook/detail/high-frequency-algorithm-exercise/
2. https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/50e446/



