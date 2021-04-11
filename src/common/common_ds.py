"""set
"""
A = set()
A.add(e)
A.remove(e)
if e not in A:
A&B #交集
A|B #并集
A-B #差集

"""dictionary
"""
dic.sort(key = lambda x:(-len(x),x)) # 排序：①长度降序；②字典序。
dic.get() # 返回指定键的值,若不存在默认返回None


"""string
在python中，str类型是不可变的
"""
str1 = str1.strip() # 删除首部空格
str1[:i]
str1[i:]
str1[::-1]

str1.count()
# 分离字符串
for ch in str2.split(",")

# 判断回文
isPalindrome = lambda s: s == s[::-1]

"""list
"""
list1 += 
list1.append()

"""matrix
"""
m,n = len(matrix),len(matrix[0]) # 矩阵的行数、列数
matrix = list(zip(*matrix)) # 矩阵转置

"""list -> str
"""
str1 = "".join(list1)

"""stack
"""
A = [1]
if A.pop() == 1:
    print(A) # 此时 A = []

"""heap
"""
A = heapify(list1)
heappush(A, num) # 小顶堆
heappush(A, -num) # 大顶堆
heappop(A)
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

"""bit operation
- python 因为位数没有限制，所以负数补码会很长，所以要位与 0xffffffff 处理成 3232 位整型数
"""
x &= x-1 # 若放在循环里，不断消去1
x<<1 # x左移1位，表示x乘以2
x>>1 # x右移1位，表示x除以2
x&1  # x和1按位与，表示x除以2的余数，即判断奇偶数
# x和自身异或结果为0，0和x异或结果还是x，用于寻找本身独一无二的数

"""中位数
"""
(arr[(n-1)//2] + arr[n//2]) / 2.0

