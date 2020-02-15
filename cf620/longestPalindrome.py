n,m = map(int, input().split())

strSet = set()
l = []
r = []
longPal = ''
for _ in range(n):
    s = input()
    t = s[::-1]
    if s == t and len(s) > len(longPal):
        longPal = s
    if t in strSet:
        l.append(s)
        r.append(t)
        strSet.remove(t)
    else:
        strSet.add(s)

r.reverse()
ls = ''.join(l)
rs = ''.join(r)
ans = ''.join([ls,longPal,rs])
print(len(ans))
print(ans)
