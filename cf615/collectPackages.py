t = int(input())
def solve():
    n = int(input())
    packages = []
    ans = ''
    for _ in range(n):
        a, b = map(int, input().split())
        packages.append((a, b))
    packages.sort()
#    print(packages)
    x = 0
    y = 0
    for px, py in packages:
        while x != px or y != py:
#            print(px, x)
            assert px >= x
            if px > x:
                x += 1
                ans += 'R'
            elif y > py:
                print("NO")
                return
            else:
                y += 1
                ans += 'U'
    print("YES")
    print(ans)

for _ in range(t):
    solve()

