## 기출문제 - 그래프이론 42. 탑승구
# i번째 비행기를 1부터 i번째 gi번째 탑승구 중 하나에 도킹해야함
# 다른 비행기가 도킹하지 않은 탑승구에만 도킹 가능

import sys
input = sys.stdin.readline

g = int(input()) # 탑승구의 수 (1부터 g까지)
p = int(input()) # 비행기의 수
arr = [0]*(p+1)
for i in range(1, p+1):
    arr[i] = int(input())

possible = [0]*(g+1) # 현재 탑승구에 도킹 가능한지 정보

answer = 0
for i in range(1, p+1):
    for j in range(arr[i], 0, -1):
        if possible[j] == 0:
            possible[j] = 1
            answer += 1
            break

print(answer)
## 문제풀이
# 그냥 본인이 도킹 가능한 탑승구 중에서 가장 큰 값으로 도킹하게 코드를 짰는데,
# 분명 예외케이스가 생길 것 같다. 정답코드는 아래와 같다.
## 개선된 코드 (서로소 집합 알고리즘 사용)
# 서로소 집합 알고리즘을 이용하면 효율적으로 해결할 수 있다.
# 도킹하는 과정을 탑승구 간 합집합 연산으로 생각하기
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# g = int(input())
# p = int(input())
#
# parent = [0] * (g+1)
# # 부모테이블을 자기 자신으로 초기화
# for i in range(1, g+1):
#     parent[i] = i
#
# result = 0
# for _ in range(p):
#     data = find_parent(parent, int(input())) # 현재 비행기의 탑승구 루트 확인
#     if data == 0: # 루트가 0이라면 도킹이 불가능한 상태를 뜻함
#         break
#     union_parent(parent, data, data-1) # 도킹 가능하다면 왼쪽집합과 합치기
#     result += 1
#
# print(result)