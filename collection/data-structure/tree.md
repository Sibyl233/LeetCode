## 树

### 定义

在单链表中，每个节点仅有一个后继节点，当节点有 **多个后继节点**，但 **只有一个前驱节点** 的时候，就变成了一棵「树」。

### 概念

- 树的节点类型：根节点、中间节点、叶节点。
- 树的节点关系：父子关系、兄弟关系、祖孙关系
- 常用定义：子树、节点深度、节点距离
- 树的类型：**二叉树**、多叉树
  - 满二叉树
  - 完全二叉树
  - 二叉搜索树

### 实现

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

### 常用操作

#### DFS 实现前/中/后序遍历

- 前序遍历：根 → 左子树 → 右子树
- 中序遍历：左子树 → 根 → 右子树
- 后序遍历：左子树 → 右子树 → 根

> Tip：在树相关的题目中多用递归来实现某些逻辑，而递归的出口条件往往是到达叶节点的时候。

```python
def preOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if node is None: 
            return
        # 前序遍历
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    res = []
    dfs(root)
    return res
    

def inOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if node is None: 
            return
        # 中序遍历
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    
    res = []
    dfs(root)
    return res

def postOrder(root: TreeNode) -> List[int]:
    def dfs(node):
        if node is None: 
            return
        # 后序遍历
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    
    res = []
    dfs(root)
    return res
```

#### BFS 实现层次遍历

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
```





