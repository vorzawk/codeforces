def solve():
    n = int(input())
    s = input()
    t = input()
    p1 = None
    p2 = None
    for i in range(n):
        if s[i] != t[i]:
            if not p1:
                p1 = (s[i],t[i])
            elif not p2:
                p2 = (s[i],t[i])
            else:
                return 0
    if p1 and p2 and p1 == p2:
        return 1
    return 0

t = int(input())
for _ in range(t):
    if solve():
        print('YES')
    else:
        print('NO')
