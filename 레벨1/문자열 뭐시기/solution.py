def solution(s):
    if 6!=len(s) and 4!=len(s):
        return False
    for i in list(s):
        try:
            j = int(i)
        except:
            return False
    return True
