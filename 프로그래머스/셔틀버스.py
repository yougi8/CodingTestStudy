# 프로그래머스 - 17678 셔틀버스
def solution(n, t, m, timetable):
    answer = ''
    # 크루들 대기 정보 (분단위로 표시)
    crew = []
    for i in range(len(timetable)):
        crew.append(int(timetable[i][0:2]) * 60 + int(timetable[i][3:5]))
    crew.sort()

    # 버스 도착 시간 정보
    bus = [540]
    for i in range(n - 1):
        bus.append(bus[i] + t)

    idx = 0  # 버스에 탈 크루의 인덱스
    for time in bus:
        cnt = 0  # 버스에 탄 크루의 수
        while cnt < m and idx < len(crew) and crew[idx] <= time:
            idx += 1  # 한명 태우고
            cnt += 1  # 버스에 탄 크루 수 추가해주기

        if cnt < m:
            con = time
        else:
            con = crew[idx - 1] - 1

    answer = str(con // 60).zfill(2) + ":" + str(con % 60).zfill(2)  # HH:MM 형식으로 맞춰주기
    return answer

solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])