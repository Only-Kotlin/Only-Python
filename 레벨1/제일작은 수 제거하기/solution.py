def solution(arr):
    ptr = 999
    temp = 999
    if len(arr) == 1:
        return [-1]
    for i in range(len(arr)):
        if arr[i] < temp:
            temp = arr[i]
            ptr = i
    del arr[ptr]
    return arr