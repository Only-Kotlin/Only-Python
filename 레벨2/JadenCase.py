def solution(s):
    word = s.split(' ')
    word = [w.capitalize() for w in word]
    answer = word[0]
    for w in word[1:]:
        answer += ' ' + w
    return answer
