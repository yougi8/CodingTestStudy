## 프로그래머스 - 연속된 부분 수열의 합 https://school.programmers.co.kr/learn/courses/30/lessons/178870
# 25.07.29. 복습
def solution(sequence, k):
    n = len(sequence)
    answer = [0, n]

    start, end = 0, 0
    # 부분합 저장할 변수 - 시작값은 배열의 첫번째 값
    part_sum = sequence[0]
    while end < n:
        # 시작값이 k보다 크다면 뒷부분 합은 볼필요도 없이 k보다 크게 된다.
        if sequence[start] > k:
            return answer

        # 부분합이 k와 같을 때
        if part_sum == k:
            # 길이가 더 짧은 값으로 업데이트
            if (end - start) < (answer[1] - answer[0]):
                answer[0] = start
                answer[1] = end

            # 부분합이 k와 일치했을 때는 부분수열의 길이는 유지한 채 오른쪽으로 한칸 민다
            # == start, end를 +1씩 해줌
            part_sum -= sequence[start]
            start += 1
            end += 1
            # end가 +1 됐을 때 out of index 될 수도 있으니 체크해주고 합 구해주기
            if end == n:
                return answer
            part_sum += sequence[end]

        # 부분합이 k보다 크다면 값을 줄여야겠지? 시작점을 한칸 오른쪽으로 옮기자
        elif part_sum > k:
            part_sum -= sequence[start]  # 합에서도 빼주자
            start += 1

        # 부분합이 k보다 작다면 값을 늘려야겠지? 종료시점을 한칸 오른쪽으로 옮기자
        else:
            end += 1
            # 똑같이 index range 체크 해주고 합에 더해주자
            if end == n:
                return answer
            part_sum += sequence[end]
    return answer
solution([1,2,3,4,5],7)
# solution([1,1,1,2,3,4,5],5)
# solution([2,2,2,2,2],6)

## 풀이
# 처음에 44점 정도로 시간초과가 났는데, 개선된 코드에서는 부분합을 part_sum이라는 변수로 선언하고 그때그때 값 하나씩 더했는데
# 시간초과났을 때는 변수선언 안하고 sum(sequence[start:end]) 이런식으로 sum을 이용했다. (시간복잡도 O(n), n은 리스트의 길이)
## 시간초과 코드
# def solution(sequence, k):
#     n = len(sequence)
#     answer = [0,n-1]
#
#     start, end = 0, 0
#
#     while start<n and end<n and start<=end:
#         if sum(sequence[start:end+1])==k:
#             if (end-start) < (answer[1]-answer[0]):
#                 answer[0] = start
#                 answer[1] = end
#                 if (end-start)==0:
#                     return answer
#             start += 1
#             end += 1
#         elif sum(sequence[start:end+1])>k:
#             start += 1
#         else:
#             end += 1
#     return answer