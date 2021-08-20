nums = list(map(int,input().split()))
n = len(nums)
idx = []
diff = []
for i in range(n):
    if nums[i] == 1:
        idx.append(i)
head = idx[0]
tail = n-1-idx[-1]

m = len(idx)
for j in range(m-1):
    diff.append(idx[j+1]-idx[j])
print(diff)

    
    


maxCnt = max(head,tail,max(diff)//2+1)       
print(maxCnt)






