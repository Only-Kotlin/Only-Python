def solution(s, n):
    low = "abcdefghijklmnopqrstuvwxyz" 
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ''
    for char in s:
        if char in low:
            ptr = low.find(char)+n 
            answer += low[ptr%26]
        elif char in up:
            ptr = up.find(char)+n
            answer += up[ptr%26]
        else: 
            answer += " "
    return answer
