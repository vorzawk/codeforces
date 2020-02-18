n,m = map(int, input().split())

strSet = set()
l = []
r = []
mid = ''
for _ in range(n):
    s = input()
    t = s[::-1]
    if s == t:
        mid = s
    elif t in strSet:
        l.append(s)
        r.append(t)
        strSet.remove(t)
    else:
        strSet.add(s)

r.reverse()
ans = ''.join(l + [mid] + r)
print(len(ans))
print(ans)
