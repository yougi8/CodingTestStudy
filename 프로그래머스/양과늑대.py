## 프로그래머스 Lv3. 양과 늑대 https://school.programmers.co.kr/learn/courses/30/lessons/92343
def solution(info, edges):
    global answer
    answer = 0
    visited = [0] * len(info)

    def dfs(sheep, wolf):
        global answer
        if sheep <= wolf:
            return
        else:
            answer = max(answer, sheep)

        for a, b in edges:
            # a;부모, b;자식
            # 부모를 방문해야만 자식을 방문할 수 있는 구조!
            if visited[a] == 1 and visited[b] == 0:
                visited[b] = 1  # 자식도 방문 처리
                if info[b] == 0:  # 양이면 양 모으기
                    dfs(sheep + 1, wolf)
                else:  # 늑대면 늑대 모으기
                    dfs(sheep, wolf + 1)
                visited[b] = 0

    visited[0] = 1
    dfs(1, 0)

    return answer

## 간만에 dfs. visited[b] = 0으로 초기화해주는 부분을 놓치면 답이 안나온다!