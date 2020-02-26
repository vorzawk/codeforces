def solve():
    a,b = map(int, input().split())
    if a == b:
        return 0
    if b > a:
        if (b-a) % 2 == 0:
            return 2
        else:
            return 1
    else:
        if (a-b) % 2 == 0:
            return 1
        else:
            return 2

t = int(input())
for _ in range(t):
    print(solve())
