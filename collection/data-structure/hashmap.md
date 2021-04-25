## 散列表

### 定义和表示

「散列表」是一种非线性数据结构，通过利用 Hash 函数将指定的「键 `key`」映射至对应的「值 `value`」，以实现高效的元素查找。

```python
# 初始化散列表
dic = {}

# 添加 key -> value 键值对
dic["a"] = 1
dic["b"] = 2
dic["c"] = 3

# 从 key 查找 value
dic["a"] # -> 1
dic["b"] # -> 2
dic["c"] # -> 3

```

### 应用
