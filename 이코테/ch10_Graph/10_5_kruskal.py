## 이코테 chapter10 그래프 이론 - 10_5 크루스칼 알고리즘
### 최소신장트리알고리즘 - 신장트리 중에서 최소 비용으로 만들 수 있는 신장트리 찾는 알고리즘
### 간선 값을 오름차순으로 정렬시키고, 사이클을 발생시키지 않으면 결과에 포함시키기
## input 예시
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
### output : 159
import sys
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a,b,parent):
    a = find(a, parent)
    b = find(b, parent)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

## 노드 v, 간선 e
v, e = map(int, sys.stdin.readline().split())

## 부모정보 자기자신으로 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

## 간선정보 저장
edge = []
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edge.append((cost,a,b)) # 간선값을 기준으로 오름차순할 것이기 때문에 cost 먼저 담기

## 간선값을 기준으로 오름차순시키기
edge.sort()

result = 0
## 사이클 발생하는지 알아보며 결과값에 포함시키기
for i in edge:
    cost, a, b = i

    # 부모노드가 같지 않다면, 사이클이 발생하지 않은 것 -> union연산하고, 간선값을 결과에 추가하기
    if find(a,parent) != find(b,parent):
        union(a,b,parent)
        result += cost

print(result)



