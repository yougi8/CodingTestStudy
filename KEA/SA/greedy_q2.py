def best_schedule(list):
    # tuple의 어떤 값을 기준으로 sort할건지 지정 (x:x[1]은 튜플의 1번 인덱스 값을 기준으로)
    # 가장 빠른 시간에 끝나는 강의를 찾는 것이 베스트 해결책
    sorted_list = sorted(list, key=lambda x:x[1]) 

    best_selection = [sorted_list[0]] # 가장 빠른 시간에 끝나는 걍의는 무조건 듣는다.

    for course in sorted_list:
        if course[0] > best_selection[-1][1]:
           best_selection.append(course)
    return best_selection

course_list = [(4,8), (3,5), (2,4), (1,4), (8,10),(6,8),(5,7),(4,5),(5,8),(9,11)]
print('최적의 강의시간 : ', best_schedule(course_list))