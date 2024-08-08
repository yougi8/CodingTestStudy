## 프로그래머스 - 베스트 앨범 https://school.programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict

def solution(genres, plays):
    answer = []

    dic = defaultdict(list)  # 장르별로 노래 재생 횟수 총합 저장 (장르-총합)
    genre_dic = defaultdict(list)  # 장르별로 노래마다 재생 횟수랑 노래번호 저장 (장르 -[재생,번호])

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in dic:
            dic[g] = dic[g] + p
            genre_dic[g].append((p, i))
        else:
            dic[g] = p
            genre_dic[g] = [(p, i)]

    plays_sorted = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for (song, i) in plays_sorted:
        genre_sorted = sorted(genre_dic[song], key=lambda x: x[0], reverse=True)
        answer.append(genre_sorted[0][1])
        if len(genre_sorted) >= 2:
            answer.append(genre_sorted[1][1])
    return answer