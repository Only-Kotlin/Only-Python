def solution(lottos, win_nums):
    first = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    dang = 0
    zero = 0
    for i in lottos:
        if i == 0:
            dang += 1
            zero += 1
        for j in win_nums:
            if i == j:
                dang += 1

    answer = [first[dang], first[dang-zero]]
    return answer