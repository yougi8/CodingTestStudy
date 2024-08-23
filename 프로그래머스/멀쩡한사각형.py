## 프로그래머스 - 멀쩡한 사각형 Lv.2 https://school.programmers.co.kr/learn/courses/30/lessons/176962
import math
def solution(w,h):
    total = w*h
    out = (w+h)-math.gcd(w,h)
    return total-out