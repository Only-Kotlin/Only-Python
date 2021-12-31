def solution(n):
    answer = [int(i) for i in str(n)]
    a = []
    for i in range(len(answer), 0, -1):
        a.append(answer[i-1])
    return a