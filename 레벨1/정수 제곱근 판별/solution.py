from math import sqrt
def solution(n):
    a = sqrt(n)
    if a - int(a) != 0:
        return -1
    answer = (a + 1)**2
    return answer