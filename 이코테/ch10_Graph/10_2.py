## 이코테 chapter10 그래프 이론 - 10_2 find함 수의 시간복잡도를 개선시키는 경로 압축 기법 소스코드
import sys

### 이 find함수에서 재귀적으로 부모값을 찾아낸 후에 부모테이블을 업데이트 시키는 방식.
def find(x, parent):
    ## 지금 본인이 루트노드가 아니라면 루트노드 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # return find(parent[x], parent)
        parent[x] = find(parent[x], parent)
    # return x
    return parent[x]

def union(a,b,parent):
    ## a,b 부모노드 찾기
    a = find(a, parent)
    b = find(b, parent)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


## 노드 v, 간선 e
v, e = map(int, sys.stdin.readline().split())
## 부모 정보 테이블 초기화 (자기 자신으로)
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

## 간선 정보만큼 Union 연산 수행
for i in range(e):
    a,b = map(int, sys.stdin.readline().split())
    union(a,b,parent)

print('각 원소가 속합 집합: ', end='')
for i in range(1, v+1):
    print(find(i, parent), end=' ')
print()
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')