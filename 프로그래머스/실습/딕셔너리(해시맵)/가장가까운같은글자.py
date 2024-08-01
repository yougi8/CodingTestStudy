## 프로그래머스 실습 - 딕셔너리 - 가장 가까운 같은 글자
from collections import defaultdict

def solution(s):
    answer = []
    dict = defaultdict(list)
    for i in range(len(s)):
        dict[s[i]].append(i)

    for i in range(len(s)):
        if s[i] in dict:
            dict[s[i]].sort(reverse=True)
            print(dict[s[i]])
            flag = -1
            for j in dict[s[i]]:
                if j < i:
                    flag = j
                    break
            if flag == -1: answer.append(-1)
            else: answer.append(i-j)
        else:
            answer.append(-1)
    print(answer)
    return answer

solution("banana")