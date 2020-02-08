t = int(input())
def solve():
    n = int(input())
    packages = []
    moves = []
    for _ in range(n):
        a, b = map(int, input().split())
        packages.append((a, b))
    packages.sort()
    x = 0
    y = 0
    for px, py in packages:
        while x != px or y != py:
            if px > x:
                x += 1
                moves.append('R')
            elif py > y:
                y += 1
                moves.append('U')
            else:
                print("NO")
                return
    print("YES")
    ans = ''.join(moves)
    print(ans)

for _ in range(t):
    solve()

