## 이코테 chapter10 그래프 이론 - 10_4 서로소집합을 활용한 사이클 판별
import sys
## 노드 v, 간선 e
v, e = map(int, sys.stdin.readline().split())

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

## 부모노드를 자기 자신으로 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(1, v+1):
    a,b = map(int, sys.stdin.readline().split())
    if find(a,parent) == find(b,parent):
        cycle = True
        break
    union(a,b,parent)


if cycle:
    print('사이클이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')


