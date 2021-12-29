def solution(x):
    good = sum([int(n) for n in str(x)])
    if x % good == 0:
        return True
    return False