def solution(s):
    answer = ""
    for word in sorted(s, reverse = True):
        answer += word
    return answer
