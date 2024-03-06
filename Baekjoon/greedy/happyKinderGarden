# 백준 13164번
import sys
def min_cost(n,k,height):
    cost = 0 # 티셔츠 만드는 최소 비용
    gap = [0]*(n-1) # 인접한 원생들의 키 차이값
    for i in range(n-1): # gap 값 구하기.
        gap[i] = height[i+1] - height[i]

    gap.sort() # 최소값을 구해야하니까 gap 리스트를 오름차순으로 정렬
    for i in range(n-k): # n명의 사람을 k개의 조로 나누려면, n-k 번만큼 나누는 과정을 실시해야 한다. (벽을 세우는 느낌)
        cost += gap[i] # 낮은 gap부터 cost에 추가하기
    return cost
n, k = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))
print(min_cost(n, k, height))