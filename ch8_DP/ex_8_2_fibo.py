visit = [0] * 100
def fibo(x):
    if x==1 or x==2:
        return 1
    if  visit[x] != 0:
        return visit[x]
    visit[x] = fibo(x-1) + fibo(x-2)
    return visit[x]
print(fibo(4))