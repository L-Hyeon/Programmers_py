def solution(price, money, count):
    res = -(money - sum(i*price for i in range(1, count + 1)))
    return res if (res > 0) else 0