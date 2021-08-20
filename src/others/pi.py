import random
def helper(n):
    cnt = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if pow(x,2)+pow(y,2)<=1:
            cnt += 1
    return cnt/n*4

if __name__ == "__main__":
    n = 100000  
    print(helper(n))
