def solution(n):
    answer = ""
    flag = 0
    for i in range(n):
        if flag == 0:
            answer = answer + "수"
            flag = 1
        else:
            answer = answer + "박"
            flag = 0

    return answer