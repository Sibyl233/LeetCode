## 时间复杂度和空间复杂度

### 概念

- 复杂度是一个动态的渐进的概念

  评估一个算法性能的好坏通常有 2 个指标：**执行时间** 和 **内存消耗**，与此相关的两个概念就是「时间复杂度」 和「空间复杂度」，**但时间（空间）复杂度不等于执行时间（内存消耗）**，因为复杂度是一个动态的渐进的概念。

- 时间复杂度的数学定义和简单表述
  - 数学定义：存在正常数 $c$ 和 $n_0$，使得对所有 $n \geq n_0$，有 $0 \leq f(n) \leq c g(n)$。这个 $f(n)$ 我们用 $O(g(n))$ 来表示，$O$ 表示的是一个函数的渐进上界。
  - 语言定义：找一个表达式比较简单的函数  $g(n)$，用 **大O表示法** 来近似地表示准确值 $f(n)$。
  - 简单表述：**算法在输入数据的规模成倍增长的时候，相应的时间消耗多增长了多少**。

- 更关注时间复杂度

  很多时候时间复杂度和空间复杂度存在类似鱼与熊掌的关系，从而有 **时间换空间** 和 **空间换时间** 两种优化思路。一般来说，用户更关心一个程序的时间效率，而不关心一个算法在后台到底占用了多少空间。估算时间复杂度的意义在于 (1)不同算法的**比较** 和 (2)自我检查**优化**。


### 计算

#### 常见时间复杂度

- 常数时间复杂度 $O(1)$

```python
def func(n):
    a = 1
```

- 线性时间复杂度 $O(n)$

```python
def func(n):
    for i in range(n):
        a = 1
```

- 多项式时间复杂度 $O(n^2)$

```python
# 多项式时间复杂度 1
def func(n):
    for i in range(n):
        for j in range(n):
            a = 1
            
# 多项式时间复杂度 2
def func(n):
    for i in range(n):
        for j in range(i, n):
            a = 1
```

- 指数时间复杂度 $O(2^n)$

```python
def func(n):
    if n <= 1: return n
    return func(n-1) + func(n-1)
```

- 对数时间复杂度 $O(logn)$

```python
def func(n):
    if n <= 1: return n
    return func(n//2)
```

- 渐进时间复杂度

```python
def func(n):
    if n <= 1: return
    mid = n // 2
    for i in range(mid+1, n):
        a = 1
    func(mid)
```

这个例子的时间复杂度为 $O(n)$。这段代码实际上表示的是：
$$
f(n)=\frac{n}{2}+\frac{n}{4}+\frac{n}{8}+\ldots \leq n
$$

- 均摊时间复杂度

```python
a = []
def func(x):
    if x == 0:
        a.append(x)
    else:
        while a:
            a.pop()           
for i in range(n):
    func(x)
```

假设有一个全局数组 `a` 和一个函数 `func`。如果输入是 0，就往数组 `a` 里放一个数；如果输入不是 0，就把 `a` 中的数全部弹出。这样经过 n 次操作以后，算法时间复杂度为 O(n) 。因为不管每次操作具体弹出多少，**总共能弹出的数的数量就是插入到数组中的数的数量**。

#### 常见计算规则

1. 基本操作，只有常数项，认为其时间复杂度为O(1)
2. 顺序结构，时间复杂度按加法进行计算
3. 循环结构，时间复杂度按乘法进行计算
4. 分支结构，时间复杂度取最大值
5. 判断一个算法的效率时，往往只需要关注操作数量的最高次项，其他次要项和常数项可以忽略
6. 在没有特殊说明时，所分析的算法的时间复杂度都是指最坏时间复杂度


### 参考

1. https://leetcode-cn.com/leetbook/read/learning-algorithms-with-leetcode/
2. https://leetcode-cn.com/leetbook/read/high-frequency-algorithm-exercise/

