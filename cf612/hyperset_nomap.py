from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
deck = set()
for _ in range(n):
    card = input().split()[0]
    deck.add(card)
ans = 0

def thirdChar(a, b):
    if a == b:
        return a
    if (a == 'S' and b == 'T') or (a == 'T' and b == 'S'):
        return 'E'
    if (a == 'S' and b == 'E') or (a == 'E' and b == 'S'):
        return 'T'
    if (a == 'E' and b == 'T') or (a == 'T' and b == 'E'):
        return 'S'

def findThird(c1, c2):
    l = []
    for i in range(k):
        l.append(thirdChar(c1[i], c2[i]))
    return ''.join(l)


for c1 in deck:
    for c2 in deck:
        if c2 > c1:
            c3 = findThird(c1, c2)
            if c3 > c2 and c3 in deck:
                ans += 1
print(ans)
