def solution(t, p):
    answer = 0
    length = len(p)

    for i in range(len(t) - length + 1):
        test = t[i:i + length]

        if int(test) <= int(p):
            answer += 1
    return answer

t = "10203"
p = "15"
print('answer : ',solution(t,p))

### 문제 풀이
# 음.. range범위 정하는거랑 test 할당할 때 인덱스 슬라이싱하는 게 범위가 헷갈려서
# 결국 파이참에서 디버깅 해보고 깨달았다...! 엉엉.....