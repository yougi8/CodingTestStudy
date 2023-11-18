def schedule_lectures(lectures):
    # 강의를 종료 시간에 따라 오름차순으로 정렬
    sorted_lectures = sorted(lectures, key=lambda x: x[1])
        # lambda 함수는 익명 함수를 생성
        # x는 lectures 리스트의 각 원소(튜플)를 가리키며, x[1]은 튜플의 두 번째 요소를 의미
        # lectures 리스트의 각 튜플을 튜플의 두 번째 요소를 기준으로 오름차순 정렬한 새로운 리스트를 sorted_lectures에 할당합니다.

    # 첫 번째 강의를 스케줄에 추가
    schedule = [sorted_lectures[0]]

    for lecture in sorted_lectures:
        # 현재 스케줄 마지막 강의의 종료 시간이 다음 강의의 시작 시간보다 이른 경우, 스케줄에 추가
        print(lecture)
        print("종료시간:", schedule[-1][1]) # 강의종료시간
        print("시작시간:", lecture[0]) # 시작시간
        # schedule[-1] : 리스트의 마지막 요소
        # schedule[-1][1] : 마지막 요소(튜플)의 2번째 값

        if schedule[-1][1] < lecture[0]:
            schedule.append(lecture)
            print(schedule)

    return schedule


lectures = [(4, 8), (3, 5), (2, 4), (1, 4), (8, 10), (6, 8), (5, 7), (4, 5), (5, 8), (9, 11)]
print(schedule_lectures(lectures))

####################################
# 리스트 정렬 함수
## sort() : 리스트 자체를 정렬
## sorted() : 원래의 리스트는 그대로 두고, 새로운 정렬된 리스트를 반환! => 원본 리스트에 영향 X
# key 매개변수 : 정렬 기준을 정의

# append() : 리스트 메서드 - 리스트의 끝에 새로운 요소 추가