t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    ans = 0
    if a > 0:
        ans += 1
        a -= 1
    if b > 0:
        ans += 1
        b -= 1
    if c > 0:
        ans += 1
        c -= 1

    if b > a:
        a,b = b,a
    if c > a:
        a,c = c,a

    if a > 0 and b > 0:
        ans += 1
        a -= 1
        b -= 1
    if a > 0 and c > 0:
        ans += 1
        a -= 1
        c -= 1
    if b > 0 and c > 0:
        ans += 1
        b -= 1
        c -= 1
    if a > 0 and c > 0 and b > 0:
        ans += 1
        a -= 1
        c -= 1
        b -= 1
    print(ans)


