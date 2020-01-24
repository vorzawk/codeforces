n = int(input())
friends = list(map(int, input().split()))
friends.insert(0, None)
u = []
setRcv = set(range(1,n+1))
for i, f in enumerate(friends):
    if f is None:
        continue
    if f == 0:
        u.append(i)
    else:
        setRcv.remove(f)
#print(u)
r = list(setRcv)
r.sort()
r.reverse()
#print(r)
numFr = len(u)

for i in range(numFr):
    if u[i] == r[i]:
        r[i], r[(i+1) % numFr] = r[(i+1) % numFr], r[i]
#print(r)

i = 0
for f in friends:
    if f is None:
        continue
    if f != 0:
        print(f, end=' ')
    else:
        print(r[i], end=' ')
        i += 1
