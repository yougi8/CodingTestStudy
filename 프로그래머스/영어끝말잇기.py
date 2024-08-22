## 프로그래머스 - 영어 끝말잇기 Lv2 https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    # 몇번째 차례인지 판단
    cnt = 1
    used = [] # 사용한 단어 리스트

    for i in range(0,len(words)-n+1,n):
        for j in range(n):
            before = words[j+i-1] # 제대로 끝말잇기 했는지 판단하려고 이전 단어 저장
            word = words[j+i] # 현재 얘가 말한 단어

            # 첫번째 순서면 암거나 말해도 됨. 사용한 단어 리스트에만 저장하고 통과
            if i==0 and j==0:
                used.append(word)
                continue

            # 만약 이미 사용한 단어를 말했거나 끝말을 잇지 않았을 때 해당 사람의 번호와 몇턴인지 출력
            if word in used or word[0]!=before[-1]:
                return [j+1,cnt]
            else:
                used.append(word)
        cnt += 1

    return [0,0]