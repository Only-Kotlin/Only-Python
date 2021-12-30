def solution(n):
    answer = ""
    a = sorted(list(map(str, str(n))), reverse=True)
    for i in a:
        answer += i
    return int(answer)