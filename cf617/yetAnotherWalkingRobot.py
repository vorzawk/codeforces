t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    dist = {(0, 0): 0}
    x = 0
    y = 0
    l = -1
    r = n
    for i,m in enumerate(s):
        if m == 'R':
            x += 1
        elif m == 'L':
            x -= 1
        elif m == 'U':
            y += 1
        else:
            y -= 1
        if (x,y) in dist:
            if (i+1 - dist[(x, y)]) < r-l+1:
                l = dist[(x, y)]
                r = i
        dist[(x,y)] = i+1
    if l == -1:
        print(-1)
    else:
        print(l+1, r+1)



            
