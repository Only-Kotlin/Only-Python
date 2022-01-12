def solution(s):
    answer = ""
    sp = s.split(" ")
    for i in sp:
        cnt = 0
        for j in i:
            if cnt % 2 == 0:
                answer += j.upper()
            else : answer += j.lower()
            cnt += 1
        answer += " "

    return answer[:-1]
