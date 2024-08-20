## 프로그래머스 - 오픈채팅방 https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []  # 최종으로 채팅방에 표시되는 배열
    flows = []  # userid, 행동 저장하기
    users = {}  # userid-닉네임 저장
    for sentence in record:
        info = list(map(str, sentence.split()))
        act, userid = info[0], info[1]

        if act == 'Enter':
            nickname = info[2]
            users[userid] = nickname
            flows.append((userid, ' 들어왔습니다.'))

        elif act == 'Leave':
            flows.append((userid, ' 나갔습니다.'))

        else:
            nickname = info[2]
            users[userid] = nickname

    for flow in flows:
        userid, act = flow[0], flow[1]
        answer.append(users[userid] + '님이' + act)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

## 들어오고, 나가고, 닉네임 변경하는 모든 플로우를 flows에 저장한다
## 저장하면서 users에 userid랑 닉네임을 매번 저장 혹은 업데이트 해준다
## 모든 record를 순회하면 최종 닉네임과 userid가 매칭되는데
## 그러면 이제 flows를 돌면서 닉네임과 행동을 answer에 저장해서 출력해주면 된다