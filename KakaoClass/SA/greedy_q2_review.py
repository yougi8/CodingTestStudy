course_list = [(4,8), (3,5), (2,4), (1,4), (8,10),(6,8),(5,7),(4,5),(5,8),(9,11)]

course_list.sort(key=lambda x:x[1])

list = [course_list[0]]

for course in course_list:
    temp = list[-1]
    # 시작하는 시간이, 앞서 수강한 강의의 끝나는 시간보다 늦으면 가능
    if course[0] > temp[1]:
        list.append(course)
print(list)