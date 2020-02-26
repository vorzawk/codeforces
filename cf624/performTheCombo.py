t = int(input())
for _ in range(t):
    ans = [0] * 26
    n,m = map(int, input().split())
    combo = input()
    misses = list(map(int, input().split()))

    subans = [[0] * 26 for _ in range(n)]
    for i in range(n):
        for c in combo[:i]:
            subans[i][ord(c) - 97] += 1

    for p in misses:
        for i in range(26):
            ans[i] += subans[p][i]

    for c in combo:
        ans[ord(c) - 97] += 1

    for num in ans:
        print(num, end=' ')
    print()



