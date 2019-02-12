def NumberOf1(n):
    cnt = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        n = n & (n - 1)
        cnt += 1
    return cnt


res = NumberOf1(-3)
print(res)