def solution(arr, divisor):
    answer = []
    flag = 0
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            flag += 1
    if flag == 0:
        answer.append(-1)
    return sorted(answer)
