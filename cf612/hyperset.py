n, k = map(int, input().split())
deck = set()
for _ in range(n):
    deck.add(input())
ans = 0

mapping = {}
s1 = {'S', 'E', 'T'}
for c1 in s1:
    for c2 in s1:
        if c1 == c2:
            continue
        s2 = {'S', 'E', 'T'}
        s2.remove(c1)
        s2.remove(c2)
        mapping[(c1, c2)] = s2.pop()

def findThird(c1, c2):
    l = []
    for i in range(k):
        if c1[i] == c2[i]:
            l.append(c1[i])
        else:
            c3 = mapping[(c1[i], c2[i])]
            l.append(c3)
    return ''.join(l)

for c1 in deck:
    for c2 in deck:
        if c1 == c2:
            continue
        c3 = findThird(c1, c2)
        if c3 in deck:
            ans += 1
print(ans//6)
