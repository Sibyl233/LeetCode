row,col,t = list(map(int,input().split()))
data = []
for _ in range(row):
    data.append(list(map(int,input().split())))

def solution(row,col,t,data):
    def backtrack(down,right,cost,t):
        if down == row or right == col:
            return
        if down < row and right < col:
            cost += data[down][right]
            if cost > t:
                return
            if down == row-1 and right == col-1:
                costs.append(cost)
                return

        backtrack(down+1,right,cost,t)
        backtrack(down,right+1,cost,t)
        return cost
    
    costs = []
    backtrack(0,0,0,t)
    if len(costs):
        print(max(costs))
    else:
        print('-1')

solution(row,col,t,data)



                

