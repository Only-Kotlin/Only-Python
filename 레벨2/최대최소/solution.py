def solution(s):
    num = s.split(' ')
    answer = []

    for n in num:
        answer.append(int(n))

    min_ = min(answer)
    max_ = max(answer)

    return str(min_) + " " +  str(max_)
