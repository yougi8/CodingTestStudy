def schedule_lectures(lectures):
    sorted_lectures = sorted(lectures, key=lambda x: x[1])

    schedule = [sorted_lectures[0]]

    for lecture in sorted_lectures:
        if schedule[-1][1] < lecture[0]:
            schedule.append(lecture)

    return schedule


lectures = [(4, 8), (3, 5), (2, 4), (1, 4), (8, 10), (6, 8), (5, 7), (4, 5), (5, 8), (9, 11)]
print(schedule_lectures(lectures))

