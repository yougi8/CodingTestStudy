## 프로그래머스 연습문제 - 성격유형검사 (99클럽 미들러 문제) level 1

def solution(survey, choices):
    answer = ''

    type = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}  # 엠비티이아이 타입

    for i in range(len(survey)):
        # 1,2,3을 선택 -> 앞의 원소가 점수를 얻는다
        if choices[i] <= 3:
            type[survey[i][0]] += 4 - choices[i]
        ### 5,6,7을 선택 -> 뒤의 원소가 점수를 얻는다
        elif choices[i] >= 5:
            type[survey[i][1]] += choices[i] - 4

    type_key = list(type.keys())
    for i in range(0, 8, 2):
        if type[type_key[i]] >= type[type_key[i + 1]]:
            answer += type_key[i]
        else:
            answer += type_key[i + 1]

    return answer

## 파이썬의 딕셔너리 활용!!! key-value!!!
# - 파이썬의 딕셔너리 활용하기
#     - dic = { ‘key’ : ‘value’ , ‘key’ : ‘value’ } 쌍으로 이루어진다
#     - dic[key] 로 value값 얻을 수 있다 (반대는 안된다) → 이거 때문에 계속 keyError났음 ㅠ
#     - 모든 key값 저장하기
#         - dic_key = list(dic.keys())
#     - 모든 value값 저장하기
#         - dic_value = list(dic.values())