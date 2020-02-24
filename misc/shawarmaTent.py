from sys import stdin
input = stdin.readline

n, sx, sy = map(int, input().split())
neighbors = [(sx+1, sy), (sx, sy+1), (sx-1, sy), (sx, sy-1)]
scores = [0,0,0,0]
for i in range(n):
    x,y = map(int, input().split())
    for i, (px,py) in enumerate(neighbors):
        if min(sx,x) <= px <= max(sx,x) and min(sy,y) <= py <= max(sy,y):
            scores[i] += 1

maxVal = 0
for i,score in enumerate(scores):
    if score > maxVal:
        maxVal = score
        ans = neighbors[i]

#print(neighbors)
print(maxVal)
print(ans[0], ans[1])


