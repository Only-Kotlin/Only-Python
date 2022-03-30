def solution(n):
    F0 = 0
    F1 = 1
    answer = 0
    for i in range(1, n):
        answer = F0 + F1
        F0 = F1
        F1 = answer
    return answer % 1234567
