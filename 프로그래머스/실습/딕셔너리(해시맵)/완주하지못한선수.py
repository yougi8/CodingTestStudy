## 프로그래머스 - 실습 - 해시 - 완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


# solution(["leo", "kiki", "eden"],["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])
# solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])