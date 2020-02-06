t = int(input())
for _ in range(t):
    s = int(input())
    ans = 0
    while s >= 10:
        rem = s % 10
        x = s - rem
        ans += x
        assert x % 10 == 0
        s -= x
        s += x // 10
    print(ans + s)


