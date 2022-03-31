def solution(answers):
    a = b = c = 0
    a_sol = [1,2,3,4,5]
    b_sol = [2,1,2,3,2,4,2,5]
    c_sol = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        a_cnt = i % 5
        b_cnt = i % 8
        c_cnt = i % 10
        if answers[i] == a_sol[a_cnt]:
            a += 1
        if answers[i] == b_sol[b_cnt]:
            b += 1
        if answers[i] == c_sol[c_cnt]:
            c += 1

    sum_list = [a,b,c]
    print(sum_list)
    tmp = max(sum_list)
    index = list(filter(lambda x : sum_list[x] == tmp, range(len(sum_list))))
    index = list(map(lambda x:x+1, index))
    return index
