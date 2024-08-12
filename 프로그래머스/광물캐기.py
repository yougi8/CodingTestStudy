## 프로그래머스 - 광물캐기

## 42점짜리 코드 - 운이 좋아서 그정도 맞은 듯
def solution(picks, minerals):
    answer = 0
    # 피로도 저장
    piro = {}
    piro[0] = {'diamond': 1, 'iron': 1, 'stone': 1}
    piro[1] = {'diamond': 5, 'iron': 1, 'stone': 1}
    piro[2] = {'diamond': 25, 'iron': 5, 'stone': 1}

    # 곡괭이 * 5 해주기
    picks[0] = picks[0] * 5
    picks[1] = picks[1] * 5
    picks[2] = picks[2] * 5

    # 캘 수 있는 광물만 남기기 (곡괭이가 모자라면 광물 못 캠)
    minerals = minerals[:sum(picks)]

    length = len(minerals)
    cnt = 0
    for i in range(len(picks)):
        while picks[i] > 0 and cnt < length:
            picks[i] -= 1
            answer += piro[i][minerals[cnt]]
            # print('plus:',i,minerals[cnt],piro[i][minerals[cnt]])
            cnt += 1
    return answer
solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]) ## result : 12