## 프로그래머스 - Lv2. 스킬트리 https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    n = len(skill)
    for skills in skill_trees:
        isTrue = True
        arr = list(skill)

        for i in skills:
            if i in skill:
                if i != arr[0]:  # skill이 과정 속에 존재하는데, 첫번째 과정이 아닐 때 : 불가능
                    isTrue = False
                    break  # 바로 종료
                else:  # skill이 과정 속에 존재하는데, 첫 번째 과정이면 : 가능
                    arr.pop(0)  # 첫번째 과정 clear

        if isTrue == True:
            answer += 1
    return answer

## 문제 풀이
# arr.pop(0)을 사용했는데, arr = list(skill)로 안 하고, deque(skill) 이렇게 해서 popleft()로 사용해도 될 것 같다