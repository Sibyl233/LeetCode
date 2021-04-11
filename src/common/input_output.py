""" 输入部分
- strip去掉左右兩端的空白符，返回str
- slipt把字串按空白符拆開，返回[str]
- map把list裡面的值對映到指定型別，返回[type]
- EOF用抓異常
"""
# 1 单样例
# 1.1 单行
a = map(lambda x:int(x), input().split())

# 1.1 多行
a = int(input())
b = int(input())
c = int(input())


# 2 多样例
# 2.1 结束条件和样例数未知
while True:
    try:
        a = map(lambda x:int(x), input().split())
    except EOFError:
        break

# 2.2 结束条件已知
while True:
    a = map(lambda x:int(x), input().split())
    if a == 0 and b == 0:
        break

# 2.3 样例数已知
cases = int(input().strip()) # cases = int(input())
for case in range(cases):
    a = map(int, input().strip().split())

""" 输出部分
"""
print(a,b)
print(a, end="")


