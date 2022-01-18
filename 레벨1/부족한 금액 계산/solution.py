def solution(price, money, count):
    hap = 0
    for i in range(1, count+1):
        hap += price * i
    if (money - hap) < 0:
        return hap - money
    return 0
