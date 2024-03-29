## 이코테 chapter 10 그래프 이론 - 실전문제 02. 팀 결성
## 2024 0329 18:52 - 19:00
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

## 0번부터 n번까지 / m개의 연산 수행
input = sys.stdin.readline
n, m = map(int, input().split())

## 같은 팀인지 확인하기 위한 부모배열. 처음엔 다 자기 자신
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

## 0 a b : 팀 합치기 연산 / 1 a b : 같은 팀 여부 확인 연산
for i in range(m):
    method, a, b = map(int, input().split())
    ## 0연산이면 팀 합치기
    if method == 0:
        union(a,b,parent)
    ## 1연산이면 같은 팀 여부 확인
    else:
        if find(a,parent) == find(b,parent):
            print("YES")
        else:
            print("NO")
