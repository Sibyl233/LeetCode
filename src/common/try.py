import queue
q = queue.Queue()
q.put(1,0)

x,y = q.get()

print(x,y)