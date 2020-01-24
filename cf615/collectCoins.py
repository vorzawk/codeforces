N = int(input())
for _ in range(N):
    a, b, c, n = map(int, input().split())
    lar = max(a, b, c)
    deficit = (lar-a) + (lar-b) + (lar-c)
    if n >= deficit and (n - deficit) % 3 == 0:
        print("YES")
    else:
        print("NO")
