## 기출문제 - 그래프 이론 q42 여행 계획
## input 예시
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
## 출력 예시 : YES

import sys
input = sys.stdin.readline
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a,b,parent):
    a = find(a,parent)
    b = find(b, parent)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 수 n, 여행지에 속한 도시의 수 m
n, m = map(int, input().split())

## 부모노드 본인으로 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

## 연결정보 받기
for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n):
        if city[j] == 1: # 1이면 연결되어있다는 것.
            union(i,j,parent) # union으로 부모 정보 업데이트 시켜주기

## 여행계획
travel = list(map(int, input().split()))

## 여행 갈 수 있는지 없는지
result = True

for i in range(m-1):
    ## 부모노드가 같지 않다면! 결국 도달할 수 없다는 뜻. 여행 못 해
    if find(travel[i], parent) != find(travel[i+1], parent):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")

## 풀이 과정
# - 어떤 방법으로든 갈 수 있는지 없는지를 판단하는 문제니까, 노드들이 같은 집합 안에 있는지를 판단하면 된다고 생각
# - → union, find 써야겠다!

