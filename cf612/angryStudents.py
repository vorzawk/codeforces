N = int(input())
for _ in range(N):
    numStudents = int(input())
    s = input()
    cnt = None
    ans = 0
    for c in s:
        if cnt is not None and c == 'P':
            cnt += 1
            ans = max(cnt, ans)
        elif c == 'A':
            cnt = 0
    print(ans)

