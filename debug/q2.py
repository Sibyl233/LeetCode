# tasks = [1,3,4]
# dependency = '0->2'

tasks = list(map(int,input().split(',')))
dependency = list(str(input()).split(','))

depend = {}
for item in dependency:
        k,v = list(map(int,item.split('->')))
        if k not in depend:
            depend[k] = [v]
        else:
            depend[k].append(v)

# def solution(tasks, depend):
#     n = len(tasks)
#     now = 0
#     time = [0]*n
#     p = 0
#     while 0 in time:
#         if p == n:
#             p = 0
#         if time[p]!=0:
#             p += 1
#             continue
#         if p in depend:
#             backup = [time[i] for i in depend[p]]
#             if 0 not in backup: #确保有依赖关系的任务已经做完
#                 now = time[p] = now+tasks[p]
#         else:
#             now = time[p] = now+tasks[p]
#         p += 1

#     res = ''
#     for i in time:
#         res+=str(i)+','
#     n = len(res)
#     print(res[:n-1])

def solution(tasks, depend):
    n = len(tasks)
    now = 0
    queue = list(range(n))
    time = [0]*n
    while queue:
        cur = queue.pop(0)
        if cur not in depend:
            now = time[cur] = now+tasks[cur]
        else:
            for task in depend[cur]:
                if task in queue:
                    queue.append(cur)
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                now = time[cur] = now+tasks[cur]


    res = ''
    for i in time:
        res+=str(i)+','
    n = len(res)
    print(res[:n-1])

solution(tasks,depend)






