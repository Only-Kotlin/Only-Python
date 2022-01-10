def solution(arr):
    temp = arr[0]
    answer = []
    answer.append(temp)
    for i in arr[1:]:
        if temp == i:
            continue
        else:
            answer.append(i)
            temp = i
    return answer
