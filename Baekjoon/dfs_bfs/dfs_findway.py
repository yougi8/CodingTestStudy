# 백준 11403 경로찾기 - 푸는 중
import sys

n = int(sys.stdin.readline()) # 정점의 개수
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

answer = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 본인으로 가는 길은 항상 존재함
        if i == j:
            answer[i][j] = 1
        # 주어진 인접행렬은 무조건 길이 있다!
        if graph[i][j] == 1:
            answer[i][j] = 1




print(graph)