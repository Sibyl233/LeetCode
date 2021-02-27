### 236-二叉树的最近公共祖先

#### 要点

1. 根据**最近公共祖先**的概念，若 root 为 p，q 的公共祖先，只可能为以下情况：

   - p 和 q 在 root 的异侧子树中
   - root = p 且 q 在 p 的左/右子树中
   - root = q 且 p 在 q 的左/右子树中

2. 本质是**后序遍历**的思想

   - 因为需要先知道左右子树的情况，然后决定向上返回什么。

3. 递归函数解析

   - 输入：root，p 和 q
   - 输出：
     1. 如果 p 和 q 都存在，则返回它们的公共祖先；
     2. 如果 p 和 q 只存在一个，则返回存在的一个；
     3. 如果 p 和 q 都不存在，则返回 null。
   - 递归入口：`lowestCommonAncestor(root.left, p, q)`
   - 递归出口：
     1. 越过叶节点，返回 null（遍历树的基本操作）
     2. 当 root = p 或 q，返回 root（为了找寻p、q是否存在）
     3. 如果 left 为空返回 right，如果 right 为空返回 left （最终结果与空的那一侧子树无关所以返回另一侧）

4. 合理性

   **在回溯过程中可认为左右子树 left 和 right 已经算出<u>结果</u>（输出）**，根据结果可以分为以下情况：

   - 如果 left 和 right 都非空：对于当前 root 来说 p 和 q 在异侧子树中，因此 root 就是它们的最近公共祖先，返回 root；
   - 如果 left 和 right 都空：对于当前 root 来说 p 和 q 都不存在于其子树中，所以返回 null；
   - 如果 left 为空且 right 非空：对于当前 root 来说 p 和 q 都不存在于其左子树
     - 若 p 和 q 都存在于右子树，因此 right 就是它们的最近公共祖先，返回 right；
     - 若 p 和 q 其中一个存在于右子树（不妨假设 q 存在于右子树），由于 left 为空，所以在当前 root 的上游必然存在一个 root = p，返回 right 供父节点继续判断；
   - 如果 right 为空且 left 非空：和 3 同理，返回 left。

#### 参考

1. [民间题解](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/)

