def solution(input_string):
    exist = []
    answer = []

    #     exist.append(input_string[0])

    #     for i in range(1,len(input_string)-1):
    #         if input_string[i+1] in exist and input_string[i]!=input_string[i+1]:
    #             answer.append(input_string[i+1])
    #         exist.append(input_string[i])

    for i in range(len(input_string) - 1):
        if input_string[i] in exist:
            answer.append(input_string[i])
        else:
            if input_string[i] != input_string[i + 1]:
                exist.append(input_string[i])
    if input_string[-1] in exist:
        answer.append(input_string[-1])

    if len(answer) == 0:
        return 'N'
    new = list(set(answer))
    new.sort()
    result = ''.join(new)
    return result