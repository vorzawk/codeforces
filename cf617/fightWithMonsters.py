from math import ceil
n, a, b, k = map(int, input().split())
h = list(map(int, input().split()))
cost = [0] * n
for i,m in enumerate(h):
    r = m % (a+b)
    # at the end of x rounds, if monster's remaining strength is within a
    if 0 < r <= a:
        continue
    # if b slayed the monster
    if r == 0:
        r += b
    else:
        r -= a
    # a cannot slay the monster, but b can coz a < r < a+b, so can't give another chance to b.
    cost[i] += ceil(r/a)
cost.sort()
ans = 0
for c in cost:
    if c <= k:
        ans += 1
        k -= c
print(ans)
    


