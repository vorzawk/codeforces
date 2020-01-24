n, k = map(int, input().split())
deck = set()
for _ in range(n):
    deck.add(input())
ans = 0
 
def findThird(c1, c2):
    l = []
    for i in range(k):
        if c1[i] == c2[i]:
            l.append(c1[i])
        else:
            s = {'S', 'E', 'T'}
            s.remove(c1[i])
            s.remove(c2[i])
            l.append(s.pop())
    return ''.join(l)
 
for c1 in deck:
    for c2 in deck:
        if c2 > c1:
            c3 = findThird(c1, c2)
            if c3 > c2 and c3 in deck:
                ans += 1
print(ans)

