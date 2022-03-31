def solution(citations):
    answer = []
    zero = 0
    for i in citations:
        if i == 0:
            zero += 1
    if zero == len(citations):
        return 0
    for c in citations:
        cnt = 0
        for h in citations:
            if h >= c:
                cnt += 1
        if c >= cnt: 
            answer.append(cnt)
    return max(answer)
