N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    res = (a + b) % 3 == 0 and 2 * a >= b
    print("YES") if res else print("NO")

